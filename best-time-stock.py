"""
    Say you have an array prices for which the ith element is the price of a given stock on day i.
    Design an algorithm to find the maximum profit.
    You may complete as many transactions as you like
    (i.e., buy one and sell one share of the stock multiple times).
"""

def maxProfit(prices):
    """Input an array prices and find the max profit.

       For example:
       >>> maxProfit([7,1,5,3,6,4])
       7
       >>> maxProfit([1,2,3,4,5])
       4
       >>> maxProfit([2,1,4,5,2,9,7])
       11
    """

    # max profit = the sum of a pair of numbers' difference
    # the 1st num should be greater than the 2nd num
    # Use linked list

    # if next num is greater than current num,
    # current_difference = next_num - current_num
    # keep checking the rest of the numbers when next number is increasing
    # if next_difference is greater than current_difference
    # replace current_diff
    # stop checking when next number decreases
    # add current_diff (which is max so far) to profit
    # move to next num and restart the process
    # to add more profit until the array ends

    profit = 0
    total_profit = 0

    if len(prices) < 2:
        raise ValueError('To have transactions, you need at least to have two prices.')

    for i in range(len(prices)-1):
        # print(i)
        if prices[i+1] >= prices[i]:
            current_diff = prices[i+1] - prices[i]
            # print(current_diff)

            if current_diff > 0:
                profit = current_diff
                total_profit += profit
                # print(total_profit)
        else:
            profit = 0

    return total_profit


#######################################################
if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY PARENS!\n")
