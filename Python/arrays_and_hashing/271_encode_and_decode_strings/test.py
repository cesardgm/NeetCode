import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_encode(self) -> None:
        solution = Solution()
        delimiter = chr(257)
        # Test encoding with empty list
        self.assertEqual(solution.encode([]), "")
        # Test encoding with one string
        self.assertEqual(solution.encode(["hello"]), f"5{delimiter}hello")
        # Test encoding with multiple strings
        self.assertEqual(solution.encode(["hello", "world"]), f"5{delimiter}hello5{delimiter}world")
        # Test encoding with varying lengths and characters
        self.assertEqual(solution.encode(["a", "ab", "abc"]), f"1{delimiter}a2{delimiter}ab3{delimiter}abc")

    def test_decode(self) -> None:
        solution = Solution()
        delimiter = chr(257)
        # Test decoding an empty string
        self.assertEqual(solution.decode(""), [])
        # Test decoding a single encoded string
        self.assertEqual(solution.decode(f"5{delimiter}hello"), ["hello"])
        # Test decoding multiple encoded strings
        self.assertEqual(solution.decode(f"5{delimiter}hello5{delimiter}world"), ["hello", "world"])
        # Test decoding with varying lengths and characters
        self.assertEqual(solution.decode(f"1{delimiter}a2{delimiter}ab3{delimiter}abc"), ["a", "ab", "abc"])

if __name__ == '__main__':
    unittest.main()
