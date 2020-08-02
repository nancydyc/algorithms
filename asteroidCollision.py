def asteroidCollision(asteroids):
    """
        - iterate through the arr
        - if curr num has the same direction as prev num: + + / - -, no collision, move on
        - put curr into output list and track list
        - if not the same direction, if prev is (-) and curr is (+), no collision, move on
        - put curr into output list and track list
        - Otherwise, compare the size,
        - if curr is smaller, explode, continue to next iteration
        - else if prev is smaller, remove the prev from output list
        - keep comparing prev num and curr until no collision/no prev, move on
        - stop when no more asteriod
        - return the output arr

    >>> asteroidCollision([1,-1,-2,-2])
    [-2, -2]

    >>> asteroidCollision([8,-8])
    []

    """
    # # My solution
    # s = []
    # i = 1
    # s.append(asteroids[0])
    # output = [asteroids[0]]

    # while s and i < len(asteroids):
    #     prev = s.pop()
    #     curr = asteroids[i]
    #     # print('#', i, 'previous asteroid', prev, 'current asteroid', curr)

    #     # nothing explode
    #     if (prev > 0 and curr > 0) or (prev < 0):
    #         output.append(curr)
    #         s.append(curr)
    #         i += 1

    #     # curr explode
    #     elif prev + curr > 0:
    #         s.append(output[-1])
    #         i += 1

    #     # prev explode
    #     elif prev + curr < 0:
    #         output.pop()
    #         if output:
    #             s.append(output[-1])
    #         # finish comparing with last prev num, curr is saved
    #         else:
    #             output.append(curr)
    #             s.append(output[-1])
    #             i += 1

    #     # both explode
    #     else:
    #         output.pop()
    #         if output:
    #             s.append(output[-1])
    #             i += 1
    #         else: # start over from next num
    #             i = i + 1
    #             if i < len(asteroids):
    #                 s.append(asteroids[i])
    #                 output.append(asteroids[i])
    #                 i += 1

    #     # print('output:', output, 'prev list-s becomes:', s)

    # return output

    # Alternative Solution
    ans = []
    for new in asteroids:
        while ans and new < 0 < ans[-1]:
            if ans[-1] < -new:
                ans.pop()
                continue
            elif ans[-1] == -new:
                ans.pop()
            break
        else: # run the block below when the condition above is not true
            ans.append(new)
        # print(ans)
    return ans

##########################################################
if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print('\n Great job! ALL TESTCASES PASSED!\n')
