import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_groupAnagrams1(self) -> None:
        # Create an instance of the Solution class
        sol: Solution = Solution()
        # Test case with typical input
        self.assertEqual(sorted(sol.groupAnagrams1(["eat", "tea", "tan", "ate", "nat", "bat"])),
                         sorted([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]))
        # Test case with all anagrams
        self.assertEqual(sorted(sol.groupAnagrams1(["abc", "bca", "cab", "bac"])),
                         sorted([["abc", "bca", "cab", "bac"]]))
        # Test case with no anagrams
        self.assertEqual(sorted(sol.groupAnagrams1(["abc", "def", "ghi"])),
                         sorted([["abc"], ["def"], ["ghi"]]))
        # Test case with empty strings
        self.assertEqual(sorted(sol.groupAnagrams1(["", "", ""])),
                         sorted([["", "", ""]]))
    
    def test_groupAnagrams2(self) -> None:
        # Create another instance of the Solution class
        sol: Solution = Solution()
        # Test case with typical input
        self.assertEqual(sorted(sol.groupAnagrams2(["eat", "tea", "tan", "ate", "nat", "bat"])),
                         sorted([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]))
        # Test case with all anagrams
        self.assertEqual(sorted(sol.groupAnagrams2(["abc", "bca", "cab", "bac"])),
                         sorted([["abc", "bca", "cab", "bac"]]))
        # Test case with no anagrams
        self.assertEqual(sorted(sol.groupAnagrams2(["abc", "def", "ghi"])),
                         sorted([["abc"], ["def"], ["ghi"]]))
        # Test case with empty strings
        self.assertEqual(sorted(sol.groupAnagrams2(["", "", ""])),
                         sorted([["", "", ""]]))

if __name__ == '__main__':
    unittest.main()

