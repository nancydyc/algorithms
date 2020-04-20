def get_products_of_all_ints_except_at_index(integers):
    """Takes a list of integers and returns a list of the products.
       for each index you want to find the product of every integer
       except the integer at that index.

       For example:
       >>> get_products_of_all_ints_except_at_index([1, 7, 3, 4])
       [84, 12, 28, 21]
    """

    total = 1

    for num in integers:
        total *= num

    products = []

    for i in integers:
        products.append(int(total / i))

    return products

#######################################################
if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY PARENS!\n")
