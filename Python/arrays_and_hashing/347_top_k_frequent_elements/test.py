import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_topKFrequent(self) -> None:
        sol = Solution()
        self.assertEqual(sol.topKFrequent([1,1,1,2,2,3], 2), [1,2], "Expected [1,2] when k=2 with input [1,1,1,2,2,3]")
        self.assertEqual(sol.topKFrequent([4,4,-1,-1], 5), [4, -1], "Expected [4, -1] when k=5 with only two unique elements")
        self.assertEqual(sol.topKFrequent([1],1), [1], "Expected [1] when k=1 with only one unqiue element")

    def test_topKFrequentSimple(self) -> None:
        sol = Solution()
        self.assertEqual(sol.topKFrequentSimple([1,1,1,2,2,3], 2), [1,2], "Expected [1,2] when k=2 with input [1,1,1,2,2,3]")
        self.assertEqual(sol.topKFrequentSimple([4,4,-1,-1], 5), [4, -1], "Expected [4, -1] when k=5 with only two unique elements")
        self.assertEqual(sol.topKFrequentSimple([1],1), [1], "Expected [1] when k=1 with only one unqiue element")

if __name__ == '__main__':
    unittest.main()
