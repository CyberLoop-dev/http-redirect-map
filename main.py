#!/usr/bin/env python3
"""Trace HTTP redirect chains without automatically following redirects."""
import argparse
import json
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse
from urllib.request import HTTPRedirectHandler, Request, build_opener


REDIRECTS = {301, 302, 303, 307, 308}


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, request, response, code, message, headers, new_url):
        return None


def resolve_location(base, location):
    return urljoin(base, location)


def is_downgrade(source, destination):
    return urlparse(source).scheme.lower() == "https" and urlparse(destination).scheme.lower() == "http"


def trace(url, max_hops=10, timeout=8):
    chain = []
    warnings = []
    seen = set()
    current = url
    opener = build_opener(NoRedirect)
    for _ in range(max_hops + 1):
        parsed = urlparse(current)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise ValueError(f"not an absolute HTTP(S) URL: {current}")
        if current in seen:
            warnings.append(f"redirect loop detected at {current}")
            break
        seen.add(current)
        request = Request(current, method="HEAD", headers={"User-Agent": "http-redirect-map/0.1"})
        try:
            response = opener.open(request, timeout=timeout)
            status, headers = response.status, response.headers
            response.close()
        except HTTPError as response:
            status, headers = response.code, response.headers
            response.close()
        except URLError as exc:
            warnings.append(f"request failed for {current}: {exc.reason}")
            break
        location = headers.get("Location")
        chain.append({"url": current, "status": status, "location": location})
        if status not in REDIRECTS or not location:
            break
        destination = resolve_location(current, location)
        if is_downgrade(current, destination):
            warnings.append(f"HTTPS downgrade: {current} -> {destination}")
        current = destination
    else:
        warnings.append(f"maximum redirect hops reached ({max_hops})")
    return chain, warnings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url")
    parser.add_argument("--max-hops", type=int, default=10)
    parser.add_argument("--timeout", type=float, default=8)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if args.max_hops < 0 or args.timeout <= 0:
        parser.error("--max-hops must be non-negative and --timeout must be positive")
    try:
        chain, warnings = trace(args.url, args.max_hops, args.timeout)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps({"chain": chain, "warnings": warnings}, indent=2))
    else:
        for index, hop in enumerate(chain, 1):
            print(f"{index:02d}. {hop['status']}  {hop['url']}")
            if hop["location"]:
                print(f"    Location: {hop['location']}")
        for warning in warnings:
            print(f"warning: {warning}")
        if not chain and not warnings:
            print("No response received.")
    return 1 if warnings else 0


if __name__ == "__main__":
    raise SystemExit(main())
