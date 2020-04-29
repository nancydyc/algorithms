def max_duffel_bag_value(cakes, capacity):
    """Given  a list of cake type tuples and a weight capacity integer,
       returns the maximum monetary value the duffel bag can hold.

       For example:
       >>> max_duffel_bag_value([(7, 160), (3, 90), (2, 15)], 20)
       555
    """

    # sort the cakes' value per kg
    # Within the capacity, take the most valuable cake
    # for the rest capacity, try the next valuable cake

    value_lst = []



#################################################################
if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU DID AMAZING JOB!\n")
