def distributeCandies(candies, num_people):
    """
        - loop through the arr and add 1 more candy each time
        - at the last distribution n, one gets n/remaining candies
        - until the remaining of the candies is 0
        - if no candy remains return the arr of last distribution

    >>> distributeCandies(7, 4)
    [1, 2, 3, 1]

    >>> distributeCandies(10, 3)
    [5, 2, 3]

    """

    arr = [0] * num_people
    candy = 0

    while candies > 0:
        for i in range(len(arr)):
            candy += 1
            candies -= candy
            if candies >= 0:
                arr[i] += candy
            else:
                candies += candy
                arr[i] += candies
                return arr

    return arr


#################################################
if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print('Suceeded!')
