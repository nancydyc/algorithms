def arraysIntersection(arr1, arr2, arr3):
    """Given three sorted arrays strictly increasing order, return a sorted array of only the integers
       that appeared in all three arrays.

       For example:
       >>> arraysIntersection([1,2,3,4,5], [1,2,5,7,9], [1,3,4,5,8])
       [1, 5]
    """
    i = 0
    j = 0
    k = 0
    intersection = []
    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] and arr1[i] == arr3[k]:
            intersection.append(arr1[i])
            i += 1
            j += 1
            k += 1

        elif arr1[i] < arr2[j] and arr1[i] < arr3[k]:
            i += 1

        elif arr1[i] > arr2[j] and arr3[k] > arr2[j]:
            j += 1

        elif arr1[i] > arr3[k] and arr2[j] > arr3[k]:
            k += 1

        elif arr1[i] < arr3[k] and arr2[j] < arr3[k]:
            i += 1
            j += 1

        elif arr1[i] < arr2[j] and arr3[k] < arr2[j]:
            i += 1
            k += 1

        else: #arr2[j] < arr1[i] and arr3[k] < arr1[i]:
            j += 1
            k += 1

    return intersection


############################################################################
if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU DID AN EXCELLENT JOB!\n")
