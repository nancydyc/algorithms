"""
Twilio Test(A) Question 1-2:
Given many prefixes numbers and various phone numbers, find matches.
If there're more than one prefixes match the phone numbers, return the longer one.
If there's no match, return empty string.
Constraints: Phone numbers are no more than 25 digits; prefixes' length is less than numbers.
"""

def match_numbers(prefixes, numbers):
    """ Given two lists of mutiple prefixes and numbers, return the longer matched prefix for each number.
        Here assume all the numbers has a '+'.

        For example:

        >>> match_numbers(['+1415123', '+44', '+14123', '+1', '+1415122'], ['+14151234567', '+9990', '+141211227'])
        ['+1415123', '', '+1']

        >>> match_numbers(['+1415', '+444', '+1412', '+1', '+1650'], [])
        []

        >>> match_numbers([], ['+1415', '+444', '+1412', '+1', '+1650'])
        ['', '', '', '', '']
    """

    # Optimize brute force solution to avoid O(n^2)

    # New Solution: there's no need to compare each prefix with every phone number
    # 1. if prefix is greater than number, never compare them
    # 2. compare the greatest prefix with phone numbers, if there is a match, add the prefix;
    # 3. after comparing, throw the prefix and the matched phone number, we don't need to compare them repeatedly.
    # In this solution, the worst case is still n * m (n = size of numbers, m = size of prefixes)
    # But the best case can be linear time O(n), when each prefix has only one number to compare and they successfully matches.


    # We start at the largest prefix and number, so we sort the two inputs
    prefixes.sort(key=int)
    sorted_nums = sorted(numbers, key=int, reverse=True)
    matches = {}
    while prefixes:
        p = prefixes.pop()

        # to compare with long phone number, we need to cut the first few digits by prefix's length
        digits = len(p)

        # only when phone numbers longer than the prefixes do we need to compare
        n = 0
        while n < len(sorted_nums) and sorted_nums[n] >= p:
            if sorted_nums[n] == p:
                matches[sorted_nums[n]] = p
                sorted_nums.pop(n)

            elif sorted_nums[n] > p:
                if sorted_nums[n][:digits] == p:
                    matches[sorted_nums[n]] = p
                    sorted_nums.pop(n)
                else:
                    n += 1

    # if no prefix matches, return empty string
    for remain_num in sorted_nums:
        matches[remain_num] = ''

    # list the prefixes according to the original order
    result = [matches[number] for number in numbers]

    return result


############################################################################
if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU DID AN EXCELLENT JOB!\n")
