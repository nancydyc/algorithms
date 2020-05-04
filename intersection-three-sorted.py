def arraysIntersection(arr1, arr2, arr3):
    """Given three sorted arrays strictly increasing order, return a sorted array of only the integers
       that appeared in all three arrays.

       For example:
       >>> arraysIntersection([1,2,3,4,5], [1,2,5,7,9], [1,3,4,5,8])
       [1, 5]
    """
    # i = 0
    # j = 0
    # k = 0
    # intersection = []
    # while i < len(arr1) and j < len(arr2) and k < len(arr3):
    #     if arr1[i] == arr2[j] and arr1[i] == arr3[k]:
    #         intersection.append(arr1[i])
    #         i += 1
    #         j += 1
    #         k += 1
    #         continue

    #     if arr1[i] < arr2[j] or arr1[i] < arr3[k]:
    #         i += 1

    #     if arr1[i] > arr2[j] or arr3[k] > arr2[j]:
    #         j += 1

    #     if arr1[i] > arr3[k] or arr2[j] > arr3[k]:
    #         k += 1

    # return intersection

    # Solution: Get the intersection of first two arrays and then use the result to get the intersection with the third array.

    def get_common(a1, a2):
        i = j = 0
        intersection = []
        while i < len(a1) and j < len(a2):
            if a1[i] == a2[j]:
                intersection.append(a1[i])
                i += 1
                j += 1

            elif a1[i] < a2[j]:
                i += 1

            else:
                j += 1
        return intersection

    common_a1_a2 = get_common(arr1, arr2)

    return get_common(common_a1_a2, arr3)




############################################################################
if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU DID AN EXCELLENT JOB!\n")
