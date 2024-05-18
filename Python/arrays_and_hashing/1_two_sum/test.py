import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
  def test_twoSumMedium(self) -> None:
    sol: Solution = Solution()
    # Test cases
    self.assertTrue(sol.twoSumMedium([2,7,11,15],9) == [0,1], "Failed test case 1")
    self.assertTrue(sol.twoSumMedium([3,2,4],6) == [1,2], "Failed test case 2")
    self.assertTrue(sol.twoSumMedium([3,3],6) == [0,1], "Failed test case 3")

  def test_twoSumFast(self) -> None:
    sol: Solution = Solution()
    # Test cases
    self.assertTrue(sol.twoSumFast([2,7,11,15],9) == [0,1], "Failed test case 1")
    self.assertTrue(sol.twoSumFast([3,2,4],6) == [1,2], "Failed test case 2")
    self.assertTrue(sol.twoSumFast([3,3],6) == [0,1], "Failed test case 3")

  def test_twoSumSlow1(self) -> None:
    sol: Solution = Solution()
    # Test cases
    self.assertTrue(sol.twoSumSlow1([2,7,11,15],9) == [0,1], "Failed test case 1")
    self.assertTrue(sol.twoSumSlow1([3,2,4],6) == [1,2], "Failed test case 2")
    self.assertTrue(sol.twoSumSlow1([3,3],6) == [0,1], "Failed test case 3")

  def test_twoSumSlow2(self) -> None:
    sol: Solution = Solution()
    # Test cases
    self.assertTrue(sol.twoSumSlow2([2,7,11,15],9) == [0,1], "Failed test case 1")
    self.assertTrue(sol.twoSumSlow2([3,2,4],6) == [1,2], "Failed test case 2")
    self.assertTrue(sol.twoSumSlow2([3,3],6) == [0,1], "Failed test case 3")

  def test_twoSumSlow3(self) -> None:
    sol: Solution = Solution()
    # Test cases
    self.assertTrue(sol.twoSumSlow3([2,7,11,15],9) == [0,1], "Failed test case 1")
    self.assertTrue(sol.twoSumSlow3([3,2,4],6) == [1,2], "Failed test case 2")
    self.assertTrue(sol.twoSumSlow3([3,3],6) == [0,1], "Failed test case 3")

if __name__ == '__main__':
  unittest.main()
