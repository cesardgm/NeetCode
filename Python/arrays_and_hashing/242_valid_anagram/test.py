import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
  def test_isAnagramFast(self) -> None:
    sol: Solution = Solution()
    # Test case where words are anagrams of each other
    self.assertTrue(sol.isAnagramFast("anagram", "nagaram"), "Failed for strings that are anagrams of each other using Fast method")
    # Test case where words are NOT anagrams of each other
    self.assertFalse(sol.isAnagramFast("aacc", "ccac"), "Failed for strings that are NOT anagrams of each other using Fast method")
    self.assertFalse(sol.isAnagramFast("rat", "car"), "Failed for strings that are NOT anagrams of each other")

  def test_isAnagramSlow(self) -> None:
    sol: Solution = Solution()
    # Test case where words are anagrams of each other
    self.assertTrue(sol.isAnagramSlow("anagram", "nagaram"), "Failed for strings that are anagrams of each other using Fast method")
    # Test case where words are NOT anagrams of each other
    self.assertFalse(sol.isAnagramSlow("aacc", "ccac"), "Failed for strings that are NOT anagrams of each other using Fast method")
    self.assertFalse(sol.isAnagramSlow("rat", "car"), "Failed for strings that are NOT anagrams of each other")

  def test_isAnagramSimple(self) -> None:
    sol: Solution = Solution()
    # Test case where words are anagrams of each other
    self.assertTrue(sol.isAnagramSimple("anagram", "nagaram"), "Failed for strings that are anagrams of each other using Fast method")
    # Test case where words are NOT anagrams of each other
    self.assertFalse(sol.isAnagramSimple("aacc", "ccac"), "Failed for strings that are NOT anagrams of each other using Fast method")
    self.assertFalse(sol.isAnagramSimple("rat", "car"), "Failed for strings that are NOT anagrams of each other")

if __name__ == '__main__':
  unittest.main()
