def check_order(take_out, dine_in, served):
    """Given three lists of integers, return True or False based on first-in-first-serve
       principle, including repeating order. If there's order not served, also return false.

       For example:
       >>> check_order([1, 3, 5], [2, 4, 6], [1, 2, 4, 6, 5, 3])
       False

       >>> check_order([1, 3, 5], [2, 4, 6], [1, 2, 3, 5, 4, 6])
       True

       >>> check_order([1, 3, 5], [1, 2, 4, 6], [1, 1, 2, 3, 5, 4, 6])
       True

       >>> check_order([1, 3, 5], [2, 4, 6], [1, 2, 3, 5, 4])
       False
    """

    # This solution assumes that there's no repeat order number

    # count_out = -1
    # count_in = -1
    # for num in served:
    #     if num in take_out:
    #         count_out += 1

    #         if count_out != take_out.index(num):
    #             return False

    #     else:
    #         count_in += 1
    #         if count_in != dine_in.index(num):
    #             return False

    # return True

    # New solution will apply if there's repeat order numbers
    count_out = 0
    count_in = 0
    max_out = len(take_out) - 1
    max_in = len(dine_in) - 1

    for num in served:
        if count_out <= max_out and num == take_out[count_out]:
            count_out += 1

        elif count_in <= max_in and num == dine_in[count_in]:
            count_in += 1

        else:
            return False

    # Check for any extra orders at the end of take_out_orders or dine_in_orders
    if count_in < len(dine_in) or count_out < len(take_out):
        return False

    return True

#######################################################
if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU DID AMAZING JOB!\n")
