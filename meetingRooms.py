from heapq import heappush, heappop, heapify

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
    # intervals.sort(key=lambda si: si[0])

    # def arrange(intervals):
    #     if len(intervals) == 0:
    #         return 0

    #     if len(intervals) == 1:
    #         return 1

    #     else:
    #         lst = []
    #         i = 1
    #         while i < len(intervals):
    #             # print(i)
    #             if intervals[i][0] < intervals[i-1][1]:
    #                 lst.append(intervals.pop(i))
    #             else:
    #                 i += 1

    #         return arrange(lst) + 1

    # return arrange(intervals)
    # runtime: n^2 worse case


# Solution: use priority queue / min heap

    intervals.sort(key=lambda si: si[0])
    free_rooms = [] # why this is min-heap

    # use one free room for the first meeting
    heappush(free_rooms, intervals[0][1])
    # print(free_rooms)
    for meeting in intervals[1:]:
        if free_rooms[0] <= meeting[0]: # if ending earlier than start
            heappop(free_rooms) # clear the earliest ending/pop index 0 (min-heap)
            # heappop remove the smallest item in heap
        heappush(free_rooms, meeting[1]) # add the new ending time/push the num to index 0 (min-heap)
        # print(free_rooms)
    return len(free_rooms)
    # the left ending times are the numbers of rooms needed


############################################################################
if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU DID AN EXCELLENT JOB!\n")


############################################################################

# [3,5,1,2] -> 1, 2, 3, 5

# from queue import PriorityQueue
