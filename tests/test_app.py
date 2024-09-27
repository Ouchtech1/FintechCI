import unittest
from app import main


class TestApp(unittest.TestCase):
    def test_main(self):
        result = main()
        self.assertIn("Bienvenue chez Fintech Solutions!", result)


if __name__ == '__main__':
    unittest.main()
