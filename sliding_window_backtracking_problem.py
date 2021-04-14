"""
    Given two strings s and t, return the minimum window in s
    which will contain all the characters in t. 
    If there is no such window in s that covers all characters in t, 
    return the empty string "".

    Note that If there is such a window, 
    it is guaranteed that there will always
    be only one unique minimum window in s.

    Example 1:

    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    Example 2:

    Input: s = "a", t = "a"
    Output: "a"
"""

# Brute force solution
# from collections import defaultdict

# def minimum_window_substring(s, t):
#     # create a dict for t, key is char, value is number of the char
#     # loop over the string,
#     # check if s[i] is in dict above 
#     # if s[j] value not 0 (i=j)
#     # if so, decrease value by 1; decrease t len by 1
#     #      increment j
#     # when t len is 0, we cover all the char in t

#     # compare the substring s[i:j] with result string
#     # if smaller, replace the result string      
#     # increment i
#     # repeat the process above

#     # Finally, return result string 
#     if t == "":
#         return ""
#     count_dict = defaultdict(int)
#     for char in t:
#         count_dict[char] += 1
#     seen = count_dict.copy()
#     # print(seen) 

#     i = j = 0
#     result_string = s 

#     while i < len(s) and len(s[i:]) >= len(t):
#         print(i, s[i])
#         if s[i] in seen:
#             print(f"starting at {s[i]}, seen reset to {seen}, t_len reset to {len(t)}, j reset to {i}")
#             t_len = len(t)
#             j = i
#             while j < len(s) and t_len > 0:
#                 print(f"Looking at {s[j]}, target string remains {t_len} char")
#                 if s[j] in seen:
#                     seen[s[j]] -= 1
#                     print(f"Decreasing by 1, {seen}")
#                     if seen[s[j]] >= 0:
#                         t_len -= 1
#                 j += 1
            
#             print("Now window is", s[i:j])
#             if t_len == 0 and len(s[i:j]) < len(result_string):
#                 result_string = s[i:j]
#                 print(result_string)
#         i += 1
#         seen = count_dict.copy()
#         print("Continue looping ***********")

#     return result_string


# print(minimum_window_substring("ADOBECODEBANC", "ABC"), "+++++++++++++++++++++++++++++++\n")
# print(minimum_window_substring("a", ""), "+++++++++++++++++++++++++++++++\n") 
  
  
# Backtracking solution
from math import inf
def minimum_window_substring(s, t):
  seen = {}
  for char in t:
    if char in seen:
      seen[char] += 1
    else:
      seen[char] = 1
  left = 0
  result = [0, inf]
  remaing_char = len(t)
  
  #Hunting phase
  for right, right_elem in enumerate(s):
    if right_elem in seen:
      seen[right_elem] -= 1   
      if seen[right_elem] >= 0:
        remaing_char -= 1
    
    #catch up phase
    while remaing_char == 0: # dict value can be neg, so remaing_char may be 0 for a few rounds
      if (result[1]-result[0]) > (right-left): 
        result[0] = left # replacing w/ smaller
        result[1] = right # substring index
        
      if s[left] in seen: # backtracking when matching char in t
        seen[s[left]] += 1
        if seen[s[left]] > 0: # not neg
          remaing_char += 1          
      left += 1     
     
  if result[1] == inf:
    return ""
  else:
    return s[result[0]: result[1]+1]
    
s = "ADOBECODEBANC"
t = "ABC"
print(minimum_window_substring(s, t))

############################################
#######  DO NOT TOUCH TEST BELOW!!!  #######
############################################

def expect(count, name, test):
    if (count == None or not isinstance(count, list) or len(count) != 2):
        count = [0, 0]
    else:
        count[1] += 1

    result = 'false'
    errMsg = None
    try:
        if test():
            result = ' true'
            count[0] += 1
    except Exception as err:
        errMsg = str(err)

    print('  ' + (str(count[1]) + ')   ') + result + ' : ' + name)
    if errMsg != None:
        print('       ' + errMsg + '\n')

def lists_equal(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    for i in range(0, len(lst1)):
        if lst1[i] != lst2[i]:
            return False
    return True

print('Minimum Window Substring Tests')
test_count = [0, 0]


def test():
    example = minimum_window_substring("ADOBECODEBANC", "ABC")
    return example == "BANC"


expect(test_count, 'should work on first example case', test)


def test():
    example = minimum_window_substring("HELLO WORLD", "FOO")
    return example == ""


expect(test_count, 'should work on second example case', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')
