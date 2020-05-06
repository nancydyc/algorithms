import random
def kClosest(points, K):
    """Find the K closest points to the origin (0, 0).

    For example:
    >>> kClosest([[1,3],[-2,2]], 1)
    [[-2, 2]]

    >>> kClosest([[3,3],[5,-1],[-2,4]], 2)
    [[3, 3], [-2, 4]]

    >>> kClosest([[-2,-5],[8,5],[-10,-3],[-7,-1],[2,-2],[2,8]], 5)
    [[2, -2], [-2, -5], [-7, -1], [2, 8], [8, 5]]

    >>> kClosest([[6,-7],[-9,-3],[10,6],[-5,-8],[-4,-10],[-3,-10],[2,-4]], 6)
    [[2, -4], [6, -7], [-5, -8], [-9, -3], [-3, -10], [-4, -10]]
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


    # Solution: quicksort -- Lomuto's partition
    # def distance(points, index):
    #     return points[index][0] ** 2 + points[index][1] ** 2

    # def helper(lst, start, end):
    #     if start >= end:
    #         return

    #     p = random.randint(start, end)
    #     pivot = distance(lst, p)
    #     lst[start], lst[p] = lst[p], lst[start]
    #     smaller = start
    #     for bigger in range(start + 1, end + 1):
    #         if distance(lst, bigger) <= distance(lst, start):
    #             smaller += 1
    #             lst[bigger], lst[smaller] = lst[smaller], lst[bigger]

    #     lst[start], lst[smaller] = lst[smaller], lst[start]

    #     helper(lst, start, smaller - 1)
    #     helper(lst, smaller + 1, bigger)

    # sorted_points = helper(points, 0, len(points) - 1)

    # return points[:K]


    # Solution: quicksort Hoare's partition
    def distance(points, index):
        return points[index][0] ** 2 + points[index][1] ** 2

    def helper(lst, start, end):
        smaller = start - 1
        bigger = end + 1
        p = random.randint(start, end)
        while True:
            smaller += 1
            while distance(lst, smaller) < distance(lst, p):
                smaller += 1

            bigger -= 1
            while distance(lst, bigger) > distance(lst, p):
                bigger -= 1

            if smaller >= bigger:
                return bigger

            lst[smaller], lst[bigger] = lst[bigger], lst[smaller]

    def quicksort(lst, start, end):
        if start < end:
            partition_index = helper(lst, start, end)
            helper(lst, start, partition_index)
            helper(lst, partition_index + 1, end)

    quicksort(points, 0, len(points) - 1)

    return points[:K]


############################################################################
if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU DID AN EXCELLENT JOB!\n")
