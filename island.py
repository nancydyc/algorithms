# 2d Map of islands


# Count the number of islands
"""
  0 0 1 1 0
  0 0 1 0 1
  1 0 0 0 1
  0 0 1 0 0

  Each row is sublist
  How to decide a big island:
  if x + 1
  if y + 1

  - iterate through each row
  - while x < len(row)
  - if arr[y][x] is 1, number + 1

    if arr[y][x-1] is also 1

 1 0 1
 1 0 0
 1 1 0

 2 0 1
 1 0 0
 1 1 0

 2 0 1
 2 0 0
 1 1 0

 2 0 1
 2 0 0
 2 1 0

 2 0 1
 2 0 0
 2 2 0


 0 0 1
 0 0 0
 0 1 0

  0,0 -> 1
  0,1
  1,0
"""


def checkItem(x,y, arr, island_number):
  if x >= len(arr) or x < 0 or y < 0 or y >= len(arr) or arr[y][x] != 1 :
    return

  if arr[y][x] == 1:
    arr[y][x] = 2 # island is checked

    checkItem(x+1, y, arr, island_number)
    checkItem(x, y+1, arr, island_number)
    chekItem(x-1, y, arr, island_number)
    checkItem(x, y-1, arr, island_number)



def count_islands(arr):
  island_number = 0

  for y in len(arr):
    for x in len(arr[0]):
      if arr[y][x] == 1: # if we find an island, we start to explore the island
        checkItem(x,y, arr, island_number)
        island_number += 1

  return island_number


# Solution: BFS
def numIslands(grid):
  # check if the grid is land or water to find the first piece of land
  # if land, check four directions
  # if still land, mark it as visited land
  # until reach boundaries/waters and stop
  # when finishing, number of islands + 1
  # check next grid if it hasn't been visited before
  # repeat the process above
  # until all the grids have been visited
  # return number

    number = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # print(f'next grid is {(row, col)}')
            if grid[row][col] == '1':
                # print(f'visit new island {(row, col)}')
                q = []
                q.append((row, col))
                grid[row][col] = '7'
                # print(f'flag new island {(row, col)}')

                while q:
                    y, x = q.pop(0) # why here needs new variable name?
                    # print(f'visit land {(y, x)}')

                    if y + 1 < len(grid) and grid[y + 1][x] == '1':
                        # print(f'surrounding land:{(y + 1, x)}')
                        q.append((y + 1, x))
                        grid[y + 1][x] = '7'

                    if x + 1 < len(grid[0]) and grid[y][x + 1] == '1':
                        # print(f'surrounding land:{(y, x + 1)}')
                        q.append((y, x + 1))
                        grid[y][x + 1] = '7'

                    if x - 1 >= 0 and grid[y][x - 1] == '1':
                        # print(f'surrounding land:{(y, x - 1)}')
                        q.append((y, x - 1))
                        grid[y][x - 1] = '7'

                    if y - 1 >= 0 and grid[y - 1][x] == '1':
                        # print(f'surrounding land:{(y - 1, x)}')
                        q.append((y - 1, x))
                        grid[y - 1][x] = '7'
                    # print('The surrounding islands to be marked off: ', q, '\n')
                number += 1
                # print(f'island number is {number}')
            # print('--------------------------')
        # print('===================================')
    return number
