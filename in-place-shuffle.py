import random

def shuffle_in_place(lst):
    """Given a list of random integers among the range of floor and ceiling numbers,
       randomly pick an integer one by one and rearrange them in order.
    """

    # pop a random number from the list
    # then append it to the end of the list
    # pop another random number from the sublist [:-1]
    # append the number to the end of the original list
    # repeat until sublist becomes empty

    sublist = lst[:]
    while sublist:
        # print(sublist)
        num = random.sample(sublist, 1)[0]
        # print(num)
        lst.remove(num)

        lst.append(num)

        sublist.remove(num)

    return lst
