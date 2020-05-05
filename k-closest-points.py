import random
def kClosest(points, K):
    """Find the K closest points to the origin (0, 0).

    For example:
    >>> kClosest([[1,3],[-2,2]], 1)
    [[-2, 2]]

    >>> kClosest([[3,3],[5,-1],[-2,4]], 2)
    [[3, 3], [-2, 4]]
    """
    # Solution: hashmap

    # distances = {}
    # for point in points:
    #     distance = point[0] ** 2 + point[1] ** 2
    #     if distance in distances:
    #         v_points = distances[distance]
    #         n_points = v_points.append(point)
    #         distances[distance] = v_points
    #     else:
    #         distances[distance] = [point]

    # closest_points = sorted(distances.items())

    # closest_points_lst = []
    # for p in closest_points:
    #     the_point = p[1]
    #     closest_points_lst.extend(the_point)
    #     # closest_points_lst.append(the_point)

    # return closest_points_lst[:K]


    # Solution: quicksort
    def distance(points, index):
        return points[index][0] ** 2 + points[index][1] ** 2

    def helper(lst, start, end):
        if start >= end:
            return

        p = random.randint(start, end)
        pivot = distance(lst, p)
        lst[start], lst[p] = lst[p], lst[start]
        smaller = start
        for bigger in range(start + 1, end + 1):
            if distance(lst, bigger) <= distance(lst, start):
                smaller += 1
                lst[bigger], lst[smaller] = lst[smaller], lst[bigger]

        lst[start], lst[smaller] = lst[smaller], lst[start]

        helper(lst, start, smaller - 1)
        helper(lst, smaller + 1, bigger)

    sorted_points = helper(points, 0, len(points) - 1)

    return points[:K]


############################################################################
if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU DID AN EXCELLENT JOB!\n")
