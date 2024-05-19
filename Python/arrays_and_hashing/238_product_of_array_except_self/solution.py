from typing import List

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    lhs_prod = [1]
    rhs_prod = [1]

    for i in range(1,n): # O(n) - loop runs n-1 times
      lhs_prod.append( lhs_prod[-1] * nums[i-1] ) # O(1) - multiplying then appending

    for i in range(n-2, -1, -1): # O(n) - loop runs n-1 times
      rhs_prod.append( rhs_prod[-1] * nums[i+1] ) # O(1) -multiplying then appending

    rhs_prod.reverse() # O(n) - reversing order of list

    result = []
    for i in range(n): # O(n) - loop runs n times
      result.append( lhs_prod[i] * rhs_prod[i] ) # O(1) - multiplying then appending

    return result
