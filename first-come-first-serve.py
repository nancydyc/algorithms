def check_order(take_out, dine_in, served):
    """Given three lists of integers, return True or False based on the numbers order
       return True as long as the larger index of the number in the served order is also
       the larger index in the original list.

       For example:
       >>> check_order([1, 3, 5], [2, 4, 6], [1, 2, 4, 6, 5, 3])
       False

       >>> check_order([1, 3, 5], [2, 4, 6], [1, 2, 3, 5, 4, 6])
       True
    """

    # check each num of the served order
    # to see which original list it belongs to
    # count the order of the number
    # get the index of the number in its original list
    # if count != index, return False



#######################################################
if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU DID AMAZING JOB!\n")
