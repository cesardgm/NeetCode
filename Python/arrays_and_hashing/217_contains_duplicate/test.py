import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_containsDuplicateFast(self) -> None:
        sol: Solution = Solution()
        # Test cases where duplicates are expected
        self.assertTrue(sol.containsDuplicateFast([1, 2, 3, 1]), "Failed for list with duplicates using Fast method")
        self.assertTrue(sol.containsDuplicateFast([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), "Failed for list with multiple duplicates using Fast method")

        # Test cases where no duplicates are expected
        self.assertFalse(sol.containsDuplicateFast([1, 2, 3, 4]), "Failed for unique list using Fast method")
        self.assertFalse(sol.containsDuplicateFast([]), "Failed for empty list using Fast method")

    def test_containsDuplicateSlow(self) -> None:
        sol: Solution = Solution()
        # Test cases where duplicates are expected
        self.assertTrue(sol.containsDuplicateSlow([1, 2, 3, 1]), "Failed for list with duplicates using Slow method")
        self.assertTrue(sol.containsDuplicateSlow([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), "Failed for list with multiple duplicates using Slow method")

        # Test cases where no duplicates are expected
        self.assertFalse(sol.containsDuplicateSlow([1, 2, 3, 4]), "Failed for unique list using Slow method")
        self.assertFalse(sol.containsDuplicateSlow([]), "Failed for empty list using Slow method")

if __name__ == '__main__':
    unittest.main()
