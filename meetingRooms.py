def minMeetingRooms(intervals):
    """Given an array of meeting time intervals consisting of start and end times
     [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

       For example,

       >>> minMeetingRooms([[0, 30],[5, 10],[15, 20]])
       2

       >>> minMeetingRooms([[7,10],[2,4]])
       1

       >>> minMeetingRooms([[9,10],[4,9],[4,17]])
       2
    """

    # sort the lst by starting time
    intervals.sort(key=lambda si: si[0])

    def arrange(intervals):
        if len(intervals) == 0:
            return 0

        if len(intervals) == 1:
            return 1

        else:
            lst = []
            i = 1
            while i < len(intervals):
                # print(i)
                if intervals[i][0] < intervals[i-1][1]:
                    lst.append(intervals.pop(i))
                else:
                    i += 1

            return arrange(lst) + 1

    return arrange(intervals)




############################################################################
if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU DID AN EXCELLENT JOB!\n")




