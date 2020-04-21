def get_products_of_all_ints_except_at_index(integers):
    """Takes a list of integers and returns a list of the products.
       for each index you want to find the product of every integer
       except the integer at that index.

       For example:
       >>> get_products_of_all_ints_except_at_index([1, 7, 3, 4])
       [84, 12, 28, 21]
    """
    # solution 1: using division
    # total = 1

    # for num in integers:
    #     total *= num

    # products = []

    # for i in integers:
    #     products.append(int(total / i))

    # return products


    #solution 2: using greedy algo
    first_half_products = [1]
    second_half_products = [1]
    products = []

    initial_product = 1
    last_product = 1

    for x in range(len(integers)-1):
        initial_product *= integers[x]
        first_half_products.append(initial_product)

    rev_ints = integers[::-1]

    for y in range(len(rev_ints)-1):
        last_product *= rev_ints[y]
        second_half_products.append(last_product)

    second_half_products.reverse()

    for x, y in zip(first_half_products, second_half_products):
        products.append(x*y)

    return products


#######################################################
if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY PARENS!\n")
