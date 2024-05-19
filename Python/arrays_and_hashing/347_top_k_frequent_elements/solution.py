from typing import List

class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    freq_dict = {}
    for num in nums: # O(n), iterating over each element in the list
      if num not in freq_dict: # O(1) average, inserting key-value pair in dictionary
        freq_dict[num] = 1
      else: # O(1) average, incrementing the value for a key in the dictionary
        freq_dict[num] += 1

    freq_list = []
    for num, freq in freq_dict.items(): # O(m), iterating over key-value pairs in dictionary where m is the number of unique elements
      freq_list.append((freq, num)) # O(1), appending to a list is constant time

    freq_list.sort(reverse=True) # O(m log m), sorting based on the number of unique elements and on the frequency value in descending order

    result = []
    k = min(k, len(freq_list)) # O(1), fetching minimum between two values is constant time
    for i in range(k): # O(k), iterating over k items
      result.append(freq_list[i][1]) # O(1), accessing and appending an element to the list is constant time

    return result


  def topKFrequentSimple(self, nums: List[int], k: int) -> List[int]:
    from collections import Counter

    frequency_map = Counter(nums)
    top_k_frequent = sorted(frequency_map, key=frequency_map.get, reverse=True)[:k]
    return top_k_frequent

"""
        # Using Counter to count the frequency of each element in the list 'nums'.
        # Counter creates a dictionary where the keys are the elements of the list
        # and the values are the counts of these elements.

        # Sorting the keys of the frequency_map based on their corresponding values (i.e., the counts),
        # in descending order. The `key=frequency_map.get` tells the sorted() function to use the count
        # of each element as the basis for sorting.
        # - frequency_map.get: A function that takes a key and returns its corresponding value from the dictionary.
        # - reverse=True: Ensures the sort is in descending order of frequency.
"""
