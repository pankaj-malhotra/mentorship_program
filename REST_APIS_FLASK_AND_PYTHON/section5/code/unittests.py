import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_hello(self):
        self.assertEqual("Hello", "Hello")


if __name__ == '__main__':
    unittest.main()
