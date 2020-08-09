def maxSubarray(nums):
    """
        - iterate through the arr
        - if adding one more num decreasing the total, don't change the largest sum
        - else update the largest sum
          -2, 1, -3, 4, -1, 2, 1, -5, 4
          sum -1,    0      1  2

        - iterate again reversely
        - repeat the same process
          -2, 1, -3, 4, -1, 2, 1
                     6      3  sum
        - return largest sum

    >>> maxSubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    6
    >>> maxSubarray([0, -3, 1, 1])
    2

    """

    # Greedy solution
    # if len(nums) == 1:
    #     return nums[0]

    # n = len(nums)
    # total = nums[0]
    # largest_sum = nums[0]
    # for i in range(1, n):
    #     total = max(nums[i], total + nums[i])
    #     largest_sum = max(largest_sum, total)

    # return largest_sum

    # Dynamic programming solution
    n = len(nums)
    max_sum = nums[0]
    for i in range(1, n):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]
        max_sum = max(nums[i], max_sum)

    return max_sum

########################################
if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\nALL TESTS PASSED! Good job!\n")
