from typing import List

class Solution:
  def twoSumMedium(self, nums: List[int], target: int) -> List[int]:
      indexed_nums = [(num, idx) for idx, num in enumerate(nums)]  # O(n), iterating through nums list
      indexed_nums.sort()  # O(n log n), sorting list of tuples

      left: int = 0
      right: int = len(nums) - 1

      while left < right:  # O(n), potential to iterate over the array in the worst case
          left_num, left_index = indexed_nums[left]
          right_num, right_index = indexed_nums[right]

          current_sum = left_num + right_num

          if current_sum == target:  # O(1), returns a list in constant time
              return [left_index, right_index]

          elif current_sum > target:
              right -= 1

          else:  # This simplifies the last conditional block
              left += 1

  def twoSumFast(self, nums: List[int], target: int) -> List[int]:
    num_dict = {}
    for idx, num in enumerate(nums): # O(n), iterating through the list once
      complement = target - num
      if complement in num_dict: # O(1), dictionary lookup is average case constant time
        seen_idx = num_dict[complement]
        current_idx = idx
        return [seen_idx, current_idx] # O(1), return a list in constant time
      num_dict[num] = idx

  def twoSumSlow1(self,nums: List[int], target: int) -> List[int]:
    index_dict = {}
    for idx, num in enumerate(nums): # O(n), iterating over each element once to create a dictionary
      index_dict[idx] = num

    for idx, num in enumerate(nums): # O(n) iterating over each element again for searching pairs
      diff = target - num
      candidates_dict = index_dict.copy() # O(n), copying the dictionary, involves duplicating all elements
      candidates_dict.pop(idx) # O(1), popping an itme from the dictionary by key is constant time

      for idx_key, value in candidates_dict.items(): # O(n) iterating over the dictionary items in the worst case
        if diff == value: # O(1), comparison operation is constant time
          return [idx, idx_key] # O(1), returning a list is constant time

  def twoSumSlow2(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)): # O(n), iterating over each element once
      diff = target - nums[i] # O(1), computing a difference is a constant time operation

      if diff in nums[i+1:]: # O(n), `in` operation can take linear time 
        idx_a = i
        idx_b = nums.index(diff, i + 1) # O(n), `index` method can take linear time
        return  [idx_a, idx_b] # O(1), return a list of two indeces is constant time operation

  def twoSumSlow3(self, nums: List[int], target: int) -> List[int]:
    for idx_a, num in enumerate(nums): # O(n), iterating over each element once
      diff = target - num # O(1), computing a difference is a constant time
      for idx_b in range(idx_a + 1, len(nums)): # O(n), iterating over reamining elements once
        if nums[idx_b] == diff: # O(1), comparison operation is constant time
          return [idx_a, idx_b] # O(1), returning a list is constant ime
