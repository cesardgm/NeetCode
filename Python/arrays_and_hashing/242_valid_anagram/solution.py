class Solution:
  def isAnagramFast(self, s: str, t: str) -> bool:
    if len(s) != len(t): # O(1), comparing the lengths
      return False

    count = {} # O(1), initializing the dictionary
    for char in s: # O(n), iterating over string s
      if char not in count: # O(1) average, could be O(n) in the worst case due to hash collisions
        count[char] = 1
      else:
        count[char] += 1

    for char in t: # O(n), iterating over string t
      if char in count: # O(1) average, could be O(n) in the worst case due to hash collisions
        count[char] -= 1
      else:
        return False # O(1), immediately returning False if char not in count

    for value in count.values(): # O(k), where k is the number of unique characters in s
      if value != 0: # O(1), checking if any count is not zero
        return False

    return True # O(1), returning True if all counts are zero

  def isAnagramSlow(self, s: str, t: str) -> bool:
    sorted_s = ''.join(sorted(s)) # O(n log n)
    sorted_t = ''.join(sorted(t)) # O(n log n)
    return sorted_s == sorted_t # O(n), comparing each character

  def isAnagramSimple(self, s: str, t: str) -> bool:
    from collections import Counter
    collection_a = Counter(s) # O(n), where n is the length of string s
    collection_b = Counter(t) # O(m), where m is the length of string t
    return collection_a == collection_b # O(n), comparing two dictionaries
