def sortedSquares(A):
    """For example:
       >>> sortedSquares([-2,-1,3])
       [1, 4, 9]
    """
#         A.sort(key=lambda num: num ** 2)

#         return [sq ** 2 for sq in A]

# two pointers
#         res = []
#         while A[0] < 0 and A[-1] >= 0:
#             if A[0] ** 2 >= A[-1] ** 2:
#                 res.append(A.pop(0) ** 2)

#             else:
#                 res.append(A.pop() ** 2)

#         res.reverse()

#         origin = [num ** 2 for num in A]
#         if max(A) < 0:
#             origin.reverse()

#         origin.extend(res)

#         return origin

# Two pointers
    N = len(A)
    # i, j: negative, positive parts
    # How to put the two pointers in the right positions, least positive and largest negative
    j = 0
    while j < N and A[j] < 0:
        j += 1
    i = j - 1
    # print(i, j)
    ans = []
    while 0 <= i and j < N:
        if A[i]**2 < A[j]**2:
            ans.append(A[i]**2)
            i -= 1
        else:
            ans.append(A[j]**2)
            j += 1

    while i >= 0:
        ans.append(A[i]**2)
        i -= 1
    while j < N:
        ans.append(A[j]**2)
        j += 1

    return ans


############################################################################
if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU DID AN EXCELLENT JOB!\n")
