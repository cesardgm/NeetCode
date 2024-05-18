from typing import List

class Solution:
  def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
    tuples = [(''.join(sorted(string)),string) for string in strs] # O(n * k log k), iterating over each string and sorting each string (where n in the number of strings and k is the max length of any string)
    anagram_dict = {}

    for sorted_chars_key, original_string_value in tuples: # O(n), iterating over each tuple element
      if sorted_chars_key not in anagram_dict: # O(1), inserting into a dictionay is average case constant time
        anagram_dict[sorted_chars_key] = [original_string_value]
      else: # O(1), appending to a list is constant time
        anagram_dict[sorted_chars_key].append(original_string_value)

    return list(anagram_dict.values()) # O(n), converting dictionary values to a list


  def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
    primes = [ \
      2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, \
      53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101 \
    ]

    letters = {chr(ord('a')+i): primes[i] for i in range(26)} # O(1), iterating over fixed range (from 0 to 25)

    anagram_map = {}
    for word in strs: # O(n), iterating over each word in the list of words
      hash_value = 1
      for char in word: # O(k), iterating over each character within a word
        if char in letters: # O(1), multiplication and dictionary lookup are constant time
          hash_value *= letters[char]
      if hash_value not in anagram_map: # O(1), inserting into a dictionary is average case constant time
        anagram_map[hash_value] = [word]
      else: # O(1), appending to alist is constant time
        anagram_map[hash_value].append(word)
    return list(anagram_map.values()) # O(n), converting dictionary values to a list

"""
    {}: These curly braces indicate the start and end of a dictionary comprehension, similar to how square brackets [ ] are used for list comprehensions.

    chr(ord('a') + i): This is the key part of each key-value pair in the dictionary.
        ord('a') returns the ASCII value (or Unicode code point) of the character 'a', which is 97.
        i is a variable that takes values from 0 to 25 (inclusive), iterating over each number in that range.
        ord('a') + i results in numbers from 97 (for 'a') to 122 (for 'z').
        chr() converts these ASCII values back to characters, so chr(ord('a') + i) generates the letters from 'a' to 'z'.

    primes[i]: This is the value part of each key-value pair in the dictionary. primes is a list of prime numbers, and primes[i] accesses the prime number at position i. Since i ranges from 0 to 25, it will fetch each prime number corresponding to each letter from 'a' to 'z'.

    for i in range(26): This is a loop within the dictionary comprehension. It iterates over the numbers 0 to 25. For each iteration, i is used to generate a letter (as the dictionary key) and to fetch the corresponding prime number (as the dictionary value).

Putting it all together, the dictionary comprehension {chr(ord('a') + i): primes[i] for i in range(26)} constructs a dictionary where each lowercase letter from 'a' to 'z' is a key, and each key is mapped to a prime number from the list primes.
"""
