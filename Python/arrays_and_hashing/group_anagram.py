def groupAnagrams(strs):
    # O(n * k log k) - iterating over each string and sorting each string (where n is the number of strings and k is the max length of any string)
    tuples = [(''.join(sorted(string)), string) for string in strs]

    anagram_dict = {}
    # O(n) - iterating over each tuple
    for key, value in tuples:
        if key not in anagram_dict:
            # O(1) - inserting into a dictionary is average case constant time
            anagram_dict[key] = [value]
        else:
            # O(1) - appending to a list is constant time
            anagram_dict[key].append(value)

    # O(n) - converting dictionary values to a list
    return list(anagram_dict.values())

# Total Complexity: O(n * k log k) where n is the number of strings and k is the maximum length of any string.
# The most time-consuming part is the sorting of each string. The operations with the dictionary and list are relatively less costly.

# List of the first 26 prime numbers
primes = [ \
  2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, \
        59, 61, 67, 71, 73, 79, 83, 89, 97, 101 \
  ]

# Assign each prime to a letter
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
letters = {chr(ord('a') + i): primes[i] for i in range(26)}

def groupAnagramsFast(strs):
    anagram_map = {}
    # O(n * k) - where n is the number of strings and k is the average length of the strings
    for word in strs:
        hash_value = 1
        # O(k) - iterate through each character in the word
        for char in word:
            if char in letters:
                # O(1) - multiplication and dictionary lookup are constant time
                hash_value *= letters[char]
        if hash_value not in anagram_map:          
            # O(1) - inserting into a dictionary is average case constant time
            anagram_map[hash_value] = [word]
        else:
            # O(1) - appending to a list is constant time
            anagram_map[hash_value].append(word)

    # O(n) - converting dictionary values to a list
    return list(anagram_map.values())

# Total Complexity: O(n * k) where n is the number of strings and k is the average length of the strings.
# This method relies on calculating a unique hash value by multiplying primes associated with each character,
# which is more efficient than sorting for anagram grouping in terms of complexity.

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
print(groupAnagramsFast(strs))
