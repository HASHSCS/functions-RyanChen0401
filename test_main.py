import unittest
from main import square, reverse_string, is_prime, factorial, find_maximum, odd_or_even, is_palindrome, find_gcd

class TestMainMethods(unittest.TestCase):

    def test_square(self):
        self.assertEqual(square(2), 4)
        self.assertEqual(square(-2), 4)
        self.assertEqual(square(0), 0)
        self.assertAlmostEqual(square(1.1), 1.21)

    def test_reverse_string(self):
        self.assertEqual(reverse_string('hello'), 'olleh')
        self.assertEqual(reverse_string('Python'), 'nohtyP')
        self.assertEqual(reverse_string(''), '')

    def test_is_prime(self):
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(4), False)
        self.assertEqual(is_prime(17), True)
        self.assertEqual(is_prime(20), False)

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(7), 5040)

    def test_find_maximum(self):
        self.assertEqual(find_maximum([1, 2, 3, 4, 5]), 5)
        self.assertEqual(find_maximum([-1, -2, -3, -4, -5]), -1)

    def test_odd_or_even(self):
        self.assertEqual(odd_or_even(3), 'Odd')
        self.assertEqual(odd_or_even(4), 'Even')

    def test_is_palindrome(self):
        self.assertEqual(is_palindrome('madam'), True)
        self.assertEqual(is_palindrome('hello'), False)
        self.assertEqual(is_palindrome(''), True)

    def test_find_gcd(self):
        self.assertEqual(find_gcd(54, 24), 6)
        self.assertEqual(find_gcd(101, 103), 1)

if __name__ == '__main__':
    unittest.main()
