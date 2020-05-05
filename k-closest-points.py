def kClosest(points, K):
    """Find the K closest points to the origin (0, 0).

    For example:
    >>> kClosest([[1,3],[-2,2]], 1)
    [[-2,2]]

    >>> kClosest([[3,3],[5,-1],[-2,4]], 2)
    [[3,3],[-2,4]]
    """
    # calculator the distance from each point to the origin
    # sort the points
    # get the point at index [:k]

    distances = {}
    for point in points:
        # print(point)
        distance = point[0] ** 2 + point[1] ** 2
        # print(distance)
        if distance in distances:
            v_points = distances[distance]
            n_points = v_points.append(point)
            distances[distance] = v_points
        else:
            distances[distance] = [point]
        # print(distances)

    # closest_points = sorted(distances.items())[:K]
    closest_points = sorted(distances.items())
    print(closest_points)

    closest_points_lst = []
    for p in closest_points:
        the_point = p[1]
        closest_points_lst.extend(the_point)
        # closest_points_lst.append(the_point)

    return closest_points_lst[:K]


############################################################################
if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU DID AN EXCELLENT JOB!\n")
