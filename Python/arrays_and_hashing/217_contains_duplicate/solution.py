from typing import List, Set

class Solution:
  def containsDuplicateFast(self, nums: List[int]) -> bool:
    nums_set: Set[int] = set(nums)  # O(n), converting list to set (duplicates removed)
    containsDuplicate: bool = len(nums) != len(nums_set)  # O(1), comparing lengths of original list and set
    return containsDuplicate

  def containsDuplicateSlow(self, nums: List[int]) -> bool:
    nums_sorted: List[int] = sorted(nums)  # O(n log n), sorting the list
    i: int = 0
    m: int = len(nums) - 1
    while i < m:  # O(n), iterating through the list
      if nums_sorted[i] == nums_sorted[i+1]:  # O(1), checking for consecutive duplicates
        return True
      i += 1
    return False  # O(1), returning False if no duplicates are found
