import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
  def test_productExceptSelf(self) -> None:
    sol: Solution = Solution()
    self.assertEqual(sol.productExceptSelf([-1,1,0,-3,3]),[0,0,9,0,0], "Input: [-1,1,0,-3,3], Expected Output: [0,0,9,0,0]")
    self.assertEqual(sol.productExceptSelf([1,2,3,4]), [24,12,8,6], "Input: [1,2,3,4], Expected Output: [24,12,8,6]")

if __name__ == '__main__':
  unittest.main()
