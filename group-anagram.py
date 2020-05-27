"""

Given an array of strings, group anagrams together.

Input: ["tea", "ate", "nap", "pan", "eat", "hat"]
Output: [["tea", "ate", "ate"], ["nap", "pan"], ["hat"]]

We can assume that all inputs will be lowercase

"""

"""
1.) Spend 5 - 15 minutes explaining your thought process. Highly recommend drawing picture/diagram of what your approach is going to be
2.) Code up your algorithm
3.) Make sure you cover edge cases
  - if the input string is empty or null
  - if the array is empty
4.) Run through your code one more time with an example

"""


"""

How do we determine if two words are anagrams of each other?

"tea" vs "eat"

"aet" vs "aet"

a.) Brute force way: Iterate through word1 and check if each letter exists in word2
  Runtime: O(N^2)

b.) Sorting: Runtime: O(K log K)

c.) runtime: O(K)

"tea":
1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0

"eat"
1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0

"hat"
1 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0


O(26) => O(1)

"""

"""
How do we group things together?

We can use dictionaries.

The key would be aet, value = ["tea", "ate", "eat]

{
  "aet" : ["tea", "ate", "eat]
  "anp" : ["nap", "pan"]
  "aht" : ["hat"]
}

{
  (1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0): ["eat", "tea", "ate"]



}

"""

# runtime: O(N K log K)
# space: O(N)
def groupAnagrams(strs):

  dict = {}

  # O(N)
  for word in strs:

    # O(K log K)
    sorted_word = "".join(sorted(word))
    # sorted can take string, but sort only take list

    if sorted_word not in dict:
      dict[sorted_word] = [word]
    else:
      dict[sorted_word].append(word)

  return list(dict.values())


#runtime: O(NK)
#space: O(N)
def groupAnagrams2(strs):

  dict = {}
  # O(N)
  for word in strs:
    nums = [0] * 26 #O(26) = O(1)
    for letter in word: # O(K)
      nums[ord(letter) - ord('a')] += 1
      ana = tuple(nums)

    if ana not in dict:
      dict[ana] = [word]
    else:
      dict[ana].append(word)

  return list(dict.values())

print(groupAnagrams2(["tea", "ate", "nap", "pan", "eat", "hat"]))
print(groupAnagrams2(["teel", "leet", "let"]))
# print(groupAnagrams([]))

"""
'a' -> 0
'b' -> 1
ord('e') - ord('a) # 4


"""
# c = 'z'
# print(ord(c) - ord('a'))


# https://leetcode.com/problems/valid-sudoku/
# bfs
# know how to do bfs traversal on a tree
