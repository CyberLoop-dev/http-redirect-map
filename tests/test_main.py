import unittest
from main import is_downgrade, resolve_location


class RedirectMapTests(unittest.TestCase):
    def test_resolves_relative_location(self):
        self.assertEqual(
            resolve_location("https://example.com/a/page", "../next"),
            "https://example.com/next"
        )

    def test_detects_https_downgrade(self):
        self.assertTrue(is_downgrade("https://example.com", "http://example.com"))
        self.assertFalse(is_downgrade("http://example.com", "https://example.com"))


if __name__ == "__main__":
    unittest.main()
