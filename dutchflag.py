"""
    The flag of the Netherlands consists of three colors: red, white and blue.
    Given balls of these three colors arranged randomly in a line (the actual number of balls does not matter),
    the task is to arrange them such that all balls of the same color are together
    and their collective color groups are in the correct order

"""

def arrange(lst):
    """Sort an array of 0, 1 and 2's but you must do this in place, in linear time and without any extra space.

       For example:
       >>> arrange([2,0,0,1,2,1])
       [0, 0, 1, 1, 2, 2]

       >>> arrange([0,1,0,2,0,1,2])
       [0, 0, 0, 1, 1, 2, 2]
    """

    lo = 0
    mid = 0
    hi = len(lst) - 1

    while mid <= hi:
        if lst[mid] == 0:
            lst[lo], lst[mid] = lst[mid], lst[lo]
            mid += 1
            lo += 1

        elif lst[mid] == 2:
            lst[hi], lst[mid] = lst[mid], lst[hi]
            hi -= 1
            # mid += 1

        else:
            mid += 1

    return lst


############################################################################
if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU DID AN EXCELLENT JOB!\n")

