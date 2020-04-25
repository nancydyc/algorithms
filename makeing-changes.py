def make_changes(amount, lst):
    """Given an amount of money and a list of coin denominations, computes the number of ways
       to make the amount of money with coins of the available denominations.

       For example:
       >>> make_changes(4, [1, 2, 3])
       4
    """

    lst.sort()

    ways = 0
    memo = set()
    for n in range(len(lst)):
        # print(lst[n])
        if lst[n] > amount:
            continue

        times = amount // lst[n]
        remainder = amount % lst[n]
        # print(times, remainder)
        if remainder == 0:
            ways += 1
            combo = [lst[n]] * times
            c = tuple(combo)
            memo.add(c)

        if remainder != 0 and remainder in lst:

            combo = [lst[n]] * times
            combo.append(remainder)
            c = tuple(combo)
            if c in memo:
                continue
            ways += 1
            memo.add(c)

        t = 1
        for i in lst[n+1:]:
            divider = 1
            r = 1
            while divider > 0 and r > 0:
                divider = (amount - lst[n] * t) // i
                r = (amount - lst[n] * t) % i
                t += 1
            # when next number involved, look for the least common multiple
            if divider == 0:
                continue

            if r == 0:
                combo = [lst[n]] * t
                combo.append(i)
                c = tuple(combo)
                if c in memo:
                    continue
                ways += 1
                memo.add(c)

    return ways


#######################################################
if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU DID AMAZING JOB!\n")
