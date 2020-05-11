"""
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

"""

def isVAlidSudoku(board):
    """Given a list of 9 lists of 9 elements, containing 1-9 or '.' without repetition
       on each row or column or 3*3 sub-boxes.

       For example:
       >>> isVAlidSudoku([
          ["5","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]
        ])
        True

       >>> isVAlidSudoku([
          ["8","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]
        ])
        False
    """

    # if there's repetition in each row/list, return False
    # if there's repetition on each column/lst[0] - lst[8], return False
    # if there's repetition on board[0:3][0:3] board[0:3][3:6] board[0:3][6:9]
                            #  board[3:6][0:3] board[3:6][3:6] board[3:6][6:9]
                            #  board[6:9][0:3] board[6:9][3:6] board[6:9][6:9],
            # return False
    # to check repetition:
    # create a count-list of '0' * 9
    # if ord(element of the row/column/subboxes) - ord('1') >= 0,
        # the result is the index of count-list
        # update the count-list at the index += 1
    # if max(count-list) > 1
    # repetition return True


# Multiple iterations:
    # def repetition(lst): # O(n)
    #     count = [0] * 9
    #     for i in lst:
    #         if ord(i) - ord('1') >= 0:
    #             count[int(i) - 1] += 1

    #     if max(count) > 1:
    #         return True

    # for row in board:
    #     if repetition(row):
    #         return False

    # c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = []
    # box1 = box2 = box3 = box4 = box5 = box6 = box7 = box8 = box9 = []

    # # Create a new board for the 2nd rule
    # columns = [[], [], [], [], [], [], [], [], []]
    # c = 0
    # while c < 9:
    #     for i in range(len(board)):
    #         columns[c].append(board[i][c])
    #     c += 1
    # # print(columns)

    # for column in columns:
    #     if repetition(column):
    #         return False

    # # Create another board for the 3rd rule
    # subboxes = [[], [], [], [], [], [], [], [], []]
    # n = 0

    # for b in board[0:3]:
    #     subboxes[n].extend(b[0:3])
    #     subboxes[n+1].extend(b[3:6])
    #     subboxes[n+2].extend(b[6:9])

    # n += 3
    # for b in board[3:6]:
    #     subboxes[n].extend(b[0:3])
    #     subboxes[n+1].extend(b[3:6])
    #     subboxes[n+2].extend(b[6:9])

    # n += 3
    # for b in board[6:9]:
    #     subboxes[n].extend(b[0:3])
    #     subboxes[n+1].extend(b[3:6])
    #     subboxes[n+2].extend(b[6:9])

    # for box in subboxes:
    #     if repetition(box):
    #         return False

    # return True


# One Iteration O(n); O(2 * n) aux space
    def repetition(count, i):
        if ord(i) - ord('1') >= 0:
            count[int(i) - 1] += 1
        if max(count) > 1:
            return True

    def subboxes(count_box, r, b, s):
        if r < 3:
            if repetition(count_box[s], board[b][r]):
                return True
        elif r < 6:
            if repetition(count_box[s+1], board[b][r]):
                return True
        else:
            if repetition(count_box[s+2], board[b][r]):
                return True

    b = 0
    count_col = [[0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9]
    count_box = [[0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9, [0] * 9]
    while b < 9:
        # print(b)
        count_row = [0] * 9
        r = 0

        while r < 9:
            if repetition(count_row, board[b][r]):
                return False

            if repetition(count_col[r], board[b][r]):
                return False

            if b < 3:
                s = 0
                if subboxes(count_box, r, b, s):
                    return False

            elif b < 6:
                s = 3
                if subboxes(count_box, r, b, s):
                    return False

            else:
                s = 6
                if subboxes(count_box, r, b, s):
                    return False

            r += 1

        b += 1

    return True


############################################################################
if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU ARE FANTASTIC!\n")
