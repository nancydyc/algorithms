def get_products_of_all_ints_except_at_index(integers):
    """Takes a list of integers and returns a list of the products.
       for each index you want to find the product of every integer
       except the integer at that index.

       For example:
       >>> get_products_of_all_ints_except_at_index([1, 7, 3, 4])
       [84, 12, 28, 21]
       >>> get_products_of_all_ints_except_at_index([1, 0, 3, 4])
       [0, 12, 0, 0]
       >>> get_products_of_all_ints_except_at_index([1, 2])
       [2, 1]
    """

    # solution 1: using division doesn't work for list containing 0
    # total = 1

    # for num in integers:
    #     total *= num

    # products = []

    # for i in integers:
    #     products.append(int(total / i))

    # return products


    # solution 2: using greedy algo
    # first_half_products = [1]
    # second_half_products = [1]
    # products = []

    # initial_product = 1
    # last_product = 1

    # for x in range(len(integers)-1):
    #     initial_product *= integers[x]
    #     first_half_products.append(initial_product)

    # rev_ints = integers[::-1]

    # for y in range(len(rev_ints)-1):
    #     last_product *= rev_ints[y]
    #     second_half_products.append(last_product)

    # second_half_products.reverse()

    # for x, y in zip(first_half_products, second_half_products):
    #     products.append(x*y)

    # return products


    # Modify solution 2 to be O(n) space
    if len(integers) < 2:
        raise IndexError('Getting the product of numbers at other '
                          'indices requires at least 2 numbers')

    products = [None] * len(integers)

    product = 1
    for i in range(len(integers)):
        products[i] = product
        product *= integers[i]

    product = 1
    for i in range(len(integers) - 1, -1, -1):
        # print(product, products[i])
        products[i] *= product
        product *= integers[i]

    return products

#######################################################
if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU DID AMAZING JOB!\n")
