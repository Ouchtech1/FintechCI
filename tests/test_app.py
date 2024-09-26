import unittest
from app import main

class TestApp(unittest.TestCase):
    def test_main(self):
        result = main()
        self.assertEqual(result, "Bienvenue chez Fintech Solutions!")

if __name__ == '__main__':
    unittest.main()
