def max_duffel_bag_value(cakes, capacity):
    """Given  a list of cake type tuples and a weight capacity integer,
       returns the maximum monetary value the duffel bag can hold.

       For example:
       >>> max_duffel_bag_value([(7, 160), (3, 90), (2, 15)], 20)
       555
       >>> max_duffel_bag_value([(7, 210), (3, 90)], 20)
       540
       >>> max_duffel_bag_value([(7, 210), (3, 90)], 0)
       0
       >>> max_duffel_bag_value([(0, 0), (3, 90)], 20)
       540
       >>> max_duffel_bag_value([(0, 10), (3, 90)], 20)
       inf
       >>> max_duffel_bag_value([(40, 3000), (3, 90)], 20)
       540
    """

    # add a cake then the current weight of the bag is added, so index increases
    # at the index of the new weight, the cake's value is added to the current value as well
    # if used another type of cake and reached the same new weight
    # the current value will be updated to new value if current value is less than the potential new vaule

    values = [i * 0 for i in range(capacity + 1) ]

    for cake in cakes:
        if cake[0] == 0 and cake[1] != 0:
            return float('inf')
        if cake[0] == 0 and cake[1] == 0:
            continue

        weight_in_bag = 0
        current_value = 0
        new_value = 0
        for weight in range(1, capacity + 1):
            if weight % cake[0] == 0:
                weight_in_bag = weight - cake[0]
                new_value = values[weight_in_bag] + cake[1]
            #     print(current_value)
                if new_value >= values[weight]:
                    values[weight] = new_value
    # print(values)
    return max(values)


#################################################################
if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU DID AMAZING JOB!\n")
