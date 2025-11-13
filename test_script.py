import unittest

class TestWeb(unittest.TestCase):
    def test_nim_exists(self):
        with open("index.html", "r", encoding="utf-8") as f:
            content = f.read()
        self.assertIn("230411100123", content, "NIM tidak ditemukan di index.html")

if __name__ == "__main__":
    unittest.main()
