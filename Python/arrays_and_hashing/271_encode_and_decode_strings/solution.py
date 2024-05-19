from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
      delimiter = chr(257) # Unicode character beyond the typical ASCII range
      encoded_string = ""
      for word in strs: # O(m), where m is the total length of all strings combined
        encoded_string += str(len(word)) + delimiter + word # O(len(word))
      return encoded_string

    def decode(self, s: str) -> List[str]:
      strs = []
      delimiter = chr(257)
      i = 0

      while i < len(s): # O(k), iterating through the length of the string
        delimiter_pos = s.find(delimiter, i) # O(k-i) per iteration, cumulatively O(k)
        if delimiter_pos == -1: # O(1), check for delimiter
          break

        length = int(s[i:delimiter_pos]) # O(d), where d is the number of digits
        start = delimiter_pos + 1
        end = start + length
        substring = s[start:end] # O(length), where slicing out the substring
        strs.append(substring)

        i = end
      return strs
