def exist(board, word):
    """
    Input:
    [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
                            ], "ABCCED" "SEE"  "ABCB"

    Output:
    True     True   False

    - loop through the board, start from 0,0
    - when seeing word[0], explore the letter haven't visited before
    - explore left, right, up, down within the boundary
    - if match with next word[idx], update the letter, keep exploring
    - else stop/return
    - when reaching len(word), return true
    - else, return false

    Test case: ABCB

                0,0, A
                /   \
                0,-1  0,1, B
                    /   \
                    0,0    0,2, C
                        /  /  \    \
                    0,1 0,3 -1,2  1,2


                    2,0, A
                /  /   \  \
                2,-1 2,1 1,0 3,0

    Test case:
    [a, b]
    [c, d]  'abcd' -> False


    """

    sublst = [False for idx in range(len(board[0]))]
    track = [sublst.copy() for num in range(len(board))]
    # track = [sublst] * len(board) # original list is also modified
    # print(track)

    word_list = list(word)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if search(board, track, word_list, i, j):
                return True
    return False

def search(board, track, word_list, i, j):
    if not word_list:
        return True

    # print(i, j)
    if i >= len(board) or i < 0 or j >= len(board[0]) or j < 0 or track[i][j]:
        return False

    print(word_list[0], board[i][j])

    if board[i][j] != word_list[0]:
        return False
    else:
        letter = word_list.pop(0)

    track[i][j] = True
    # print(track)

    res1 = search(board, track, word_list, i, j - 1)

    res2 = search(board, track, word_list, i, j + 1)

    res3 = search(board, track, word_list, i - 1, j)

    res4 = search(board, track, word_list, i + 1, j)

    if res1 or res2 or res3 or res4:
        return True
    else:
        word_list.insert(0, letter)
        track[i][j] = False
        # print('finish searching', word_list, track)
        return False



# print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")) # False

print(exist([["a","b"],["c","d"]], "abdc")) # True

print(exist([["a","b"],["c","d"]], "abcd")) # False


# Alternative Solution A
def help(self, board, word, visited, word_position, x, y, rows, columns):
    if x < 0 or x >= rows or y < 0 or y >= columns or visited[x][y] == 1 or board[x][y] != word[word_position]:
        return False
    word_position += 1
    if word_position == len(word):
        return True
    visited[x][y] = 1
    result = help(board, word, visited, word_position, x - 1, y, rows, columns) or \
             help(board, word, visited, word_position, x + 1, y, rows, columns) or \
             help(board, word, visited, word_position, x, y - 1, rows, columns) or \
             help(board, word, visited, word_position, x, y + 1, rows, columns)

    visited[x][y] = 0
    return result

def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    rows = len(board)
    columns = len(board[0])
    visited = [[0 for i in range(columns)] for j in range(rows)]
    word_position = 0
    for row in range(rows):
        for column in range(columns):
            result = help(board, word, visited, word_position, row, column, rows, columns)
            if result:
                return True
    return False


# Alternative B
def backtrack(board, r, c, suffix):
    if len(suffix) == 0:
        return True
    if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) \
        or board[r][c] != suffix[0]:
        return False
    board[r][c] = '*'
    for row_offset, col_offset in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
        if backtrack(board, r+row_offset, c+col_offset, suffix[1:]):
            return True
    board[r][c] = suffix[0]
    return False

def exist(board, word):
    # iterate through board looking for first letter, then snake through
    if len(board) == 0 or len(board[0]) == 0 or len(word) == 0:
        return False

    for r in range(len(board)):
        for c in range(len(board[0])):
            if backtrack(board, r, c, word):
                return True

    return False
