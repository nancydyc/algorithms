# class Change():
#     def __init__(self):
#         self.memo = {}

#     def make_changes(self, amount, lst, index=0):
#         """Given an amount of money and a list of coin denominations, computes the number of ways
#            to make the amount of money with coins of the available denominations.

#            For example:
#            >>> Change().make_changes(5, [1, 2])
#            3
#            >>> Change().make_changes(4, [1, 2, 3])
#            4
#            >>> Change().make_changes(8, [2, 10, 5, 1])
#            7
#         """

#         # Solution -- Top down
#         # subproblem: seeing how many ways we can get the remaining amount
#         # from the remaining denominations
#         memo_key = str((amount, index))
#         if memo_key in self.memo:
#             return self.memo[memo_key]

#         if amount == 0:
#             return 1

#         if amount < 0:
#             return 0
#         if index >= len(lst): # out of different coins
#             return 0

#         cur_val = lst[index]

#         ways = 0

#         while amount >= 0:
#             ways += self.make_changes(amount, lst, index + 1)

#             amount -= cur_val

#         self.memo[memo_key] = ways
#         return ways


    # Solution -- Bottom up
def making_changes(amount, lst):
    """Given an amount of money and a list of coin denominations, computes the number of ways
       to make the amount of money with coins of the available denominations.

       For example:
       >>> making_changes(5, [1, 2])
       3
       >>> making_changes(4, [1, 2, 3])
       4
       >>> making_changes(8, [2, 10, 5, 1])
       7
    """
    # making a list ways_of_doing_n_cents, where the index is the amount
    # and the value at each index is the number of ways of getting that amount3
    # start with the first coin in denominations,
    # then add in the second coin, then the third, etc

    # ways of making n cents with some coin
    ways = [0 for i in range(amount + 1)]
    ways[0] = 1

    # use coin by coin in the list, increase the number of each coin
    for coin in lst:

        for higher_value in range(coin, amount + 1):
            # print(coin, higher_value)
            higher_value_remainder = higher_value - coin
            ways[higher_value] += (
                ways[higher_value_remainder]
            )
            print(ways)

    return ways[amount]


#######################################################
if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU DID AMAZING JOB!\n")
