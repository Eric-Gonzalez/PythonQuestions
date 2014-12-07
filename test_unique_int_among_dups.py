import unittest
from unique_int_amoung_dups import find_unique


class UniqueTest(unittest.TestCase):
    example_data = []

    def setUp(self):
        for i in xrange(100):
            self.example_data.append(i)
            self.example_data.append(i)


    def test_no_missing(self):
        with self.assertRaises(AttributeError):
            find_unique(self.example_data)


    def test_unique(self):
        # Remove 50 from the test data.
        self.example_data.remove(50)
        self.assertEqual(50, find_unique(self.example_data))


if __name__ == '__main__':
    unittest.main()

