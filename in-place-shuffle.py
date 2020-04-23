import random

def get_random(floor, ceiling):
    # ceiling is exclusive
    return random.randrange(floor, ceiling + 1)

def shuffle_in_place(lst):
    """Given a list of random integers among the range of floor and ceiling numbers,
       randomly pick an integer one by one and rearrange them in order.
    """

    # pop a random number from the list
    # then append it to the end of the list
    # pop another random number from the sublist [:-1]
    # append the number to the end of the original list
    # repeat until sublist becomes empty

    # MY Solution

    # sublist = lst[:]
    # while sublist:
    #     # print(sublist)
    #     num = random.sample(sublist, 1)[0]
    #     # print(num)
    #     lst.remove(num)

    #     lst.append(num)

    #     sublist.remove(num)

    # return lst


    # Solution: Fisher-Yates Shuffle/Knuth Shuffle Algorithm

    if len(lst) <= 1:
        return lst
    # search through the index for a random index instead of a random number
    for i in range(0, len(lst) - 1):
        random_index = get_random(i, len(lst) - 1)

        if random_index != i:
            lst[i], lst[random_index] = \
            lst[random_index], lst[i]

    return lst
