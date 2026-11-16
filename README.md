<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:111827,100:#22d3ee&height=180&section=header&text=HTTP%20Redirect%20Map&fontSize=42&fontColor=ffffff" alt="HTTP Redirect Map banner"/></p>
<p align="center"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1000&color=22D3EE&center=true&vCenter=true&width=650&lines=See%20every%20hop%20between%20a%20URL%20and%20its%20destination." alt="Animated project tagline"/></p>
<p align="center"><img src="https://img.shields.io/github/license/CyberLoop-dev/http-redirect-map?style=for-the-badge" alt="License"/> <img src="https://img.shields.io/github/languages/top/CyberLoop-dev/http-redirect-map?style=for-the-badge" alt="Top language"/> <img src="https://img.shields.io/github/stars/CyberLoop-dev/http-redirect-map?style=for-the-badge" alt="Stars"/> <img src="https://img.shields.io/github/last-commit/CyberLoop-dev/http-redirect-map?style=for-the-badge" alt="Last commit"/></p>
<p align="center"><img src="./assets/icon.svg" width="150" alt="HTTP Redirect Map illustration"/></p>

## 🚀 Overview

HTTP Redirect Map follows a URL one redirect at a time and prints each response status and Location target. It helps developers diagnose redirect loops, long chains, and accidental HTTPS downgrades.

## ✨ Features

- 🧭 Trace 301, 302, 303, 307, and 308 responses
- 🔗 Resolve relative Location headers correctly
- ♻️ Detect loops and enforce a maximum hop count
- 🔐 Warn when a redirect downgrades HTTPS to HTTP

## 🎬 Demo

~~~bash
python main.py https://example.com --max-hops 8
~~~

The tool sends HEAD requests and does not automatically follow redirects.

## ⚡ Quick Start

~~~bash
git clone https://github.com/CyberLoop-dev/http-redirect-map.git
cd http-redirect-map
python main.py --help
~~~

Python 3.10 or newer is recommended. Network access is needed only for tracing a target URL.

## 🧰 Tech Stack

- 🐍 Python 3.10+
- 📦 Python standard library only
- 🧪 unittest for tests

## 📁 Folder Structure

~~~text
http-redirect-map/
├── assets/icon.svg
├── tests/test_main.py
├── .gitignore
├── LICENSE
├── README.md
├── main.py
├── pyproject.toml
└── requirements.txt
~~~

## 🗺️ Roadmap

- [x] 🧩 Working redirect tracer
- [x] 🧪 Standard-library tests
- [ ] 📊 Optional HTML chain report
- [ ] 🧰 More response edge cases

## 🤝 Contributing

Issues and pull requests are welcome. Keep changes focused, add tests for new behavior, and use clear commit messages.

## 📄 License

Released under the MIT License. See [LICENSE](LICENSE).

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:#22d3ee,100:111827&height=110&section=footer" alt="Animated wave footer"/></p>
