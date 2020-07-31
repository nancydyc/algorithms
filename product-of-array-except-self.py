def productExceptSelf(nums):
    """
        Input : [1,2,3,4]

        idx
        0 - 2*3*4
        1 - 1*3*4
        2 - 1*2*4
        3 - 1*2*3

        Output: [24, 12, 8, 6]

        brute force: n^2
        - loop over the nums arr
        - get all the numbers except itself
        - calculate the product and add to output list

        slide window: O(n) !!! division should avoid 0
        - get the product of nums[1:]
        - loop over the arr
        - multiply each nums[i]      [1:] * [0]  res * [1]    res* [2]
        - divide the nums[i+1]       [1:] / [1]  res / [2]    res/ [3]
                               res = [0] [2:]    [0, 1] [3:]  [0,1,3] []

        - if nums[i] is 0, the rest of the product are all 0
        - if nums[i+1] is 0,  get the rest nums product
        - if there're more than one 0, all the products are 0

        multiply only -- left * right: O(n) runtime with space O(n)
        - for each idx
        - multiply one more num on the left side in nums[:idx]
        - save the left total result
        - for another round each index
        - multiply one more num on the right side in nums[idx + 1: :-1]
        - (reversely) add to right total result
        - merge the two lists to the final output

        Two for loop: space O(1)
        - construct an output list and update the list
        - One loop from left to the 2nd to the last num
        - Another loop from right to left to the 2nd num

    >>> productExceptSelf([1, 2, 3, 4])
    [24, 12, 8, 6]

    >>> productExceptSelf([0, 0])
    [0, 0]

    >>> productExceptSelf([1, 0])
    [0, 1]

    """

    output = [0 for i in range(len(nums))]
    if nums.count(0) > 1:
        return output

    if nums.count(0) == 1:
        idx = nums.index(0)
        total_except_zero = 1
        for num in nums[:idx]:
            total_except_zero *= num

        for num in nums[idx + 1:]:
            total_except_zero *= num

        output[idx] = total_except_zero
        return output

    total = 1
    for t in nums[1:]:
        total *= t
    output[0] = total

    for j in range(len(nums) - 1):
        total *= nums[j]
        total /= nums[j + 1]
        output[j + 1] = int(total)

    return output

###############################################
if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print('\n ALL TESTS PASSED. Great job! Succeed!\n')
