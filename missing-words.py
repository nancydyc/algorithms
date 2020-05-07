# Complete the 'missingWords' function below.#

def missingWords(s, t):
    """The function is expected to return a STRING_ARRAY.

       For example:
       >>> missingWords('I like cheese', 'I cheese')
       like

       >>> missingWords('I am using HackerRank to improve programming', 'am HackerRank to improve')
       I
       using
       programming
    """
    # move the pointers forward for s, t
    # if the words are the same, keep moving the two pointer
    # if not
    # the word of s will be added to result list
    # and the pointer of s will move until find the same as the word in t
    # when reaching the end of t
    # return the final list

    s_lst = s.split(' ')
    t_lst = t.split(' ')
    # print(s_lst, t_lst)

    s_pointer = 0
    t_pointer = 0
    res = []

    # while t_pointer <= len(t_lst):
    while s_pointer <= len(s_lst) -1 and t_pointer <= len(t_lst) -1:
        # print(s_pointer)
        # print(t_pointer)
        if s_lst[s_pointer] == t_lst[t_pointer]:
            s_pointer += 1
            t_pointer += 1
        else: #s_lst[s_pointer] != t_lst[t_pointer]
            res.append(s_lst[s_pointer])
            s_pointer += 1

    res.extend(s_lst[s_pointer:])

    r = '\n'.join(res)

    return print(r)


############################################################################
if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU DID AN EXCELLENT JOB!\n")
