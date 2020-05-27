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
  if x > len(arr) or x < 0 or y < 0 or y > len(arr) or arr[y][x] != 1 :
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
