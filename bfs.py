"""


         A

    C        B

E         F     G

       H


BFS (level order traversal) = [A, C, B, E, F, G, H]

preorder = [A, C, E, B, F, H, G]
postorder = [E, C, H, F, G, B, A]
inorder = [E, C, A, H, F, B G]


BFS: Iteration
1. Queue: FIFO (First In First Out)

    [A] => remove A => add children of A
    [C, B] => remove C => add children of C
    [B, E] => remove B => add children of B
    [E, F, G] => remove E => add children of E
    [F, G] => remove F => add children of F
    [G, H] => remove G => add children of G
    [H] => remove H => add children of H
    []

    A, C, B, E, F, G, H


2. Set/HashMap
  - So that we don't revisit nodes that have already been seen/explored. This is to avoid infinite loop when we are traversing through a cyclical graph

  Everytime we see a new node, we are going to mark it as visited in our set. We only add things to our queue if the node has not been seen/explored

  You cannot assume the graph is acyclical, unless the interviewer tells you it is acyclical

Use Case:
1.) If you want to find the minimum distance/moves from root node to some other node
2.) If a path exists between 2 nodes
3.) If you need to add things in a layer-like fashion


---------------------------------
Problem: You are given a mxn matrix, where each value in the matrix tells you how many steps you can take. You can move left, right, down, and up.

The goal is you want to find the minimum number of moves to go from top left of matrix to bottom right of matrix.

Assume that the values in the cell are non-negative. Return -1 if no such path exists.

Input:
[
  [2, 0, 1]
  [1, 3, 1]
  [2, 0, 0]

]

Output: 2
2 -> 1 -> 1- > 0 (3 moves)
2 -> 2 -> 0 (2 moves)



Input 2:
[
  [3, 1, 0, 2, 1],
  [3, 1, 3, 1, 0]
]
Output 2: 6

3 -> 2 -> 1 -> 1 -> 3 -> 1 -> 0


"""

"""
Steps:
1. topleft is root, lst[0][0]
2. lst[0][0], move to next node according to the Value
3. to check boundaries:
    right: < len(sub)
    left: < 0
    up: < 0 of the outer list
    down: len of outer list

4. how to pick next move:


  [2, 0, 1]
  [1, 3, 1]
  [2, 0, 0]

               (0,0) = 2
              q = [(2,0), (0,2)]
              moves = 1

        (2,0) = 2            (0,2) = 1
    q = [(0,2), (2,2)]       q = [(2,2), (0,1), (1,2)]
    moves = 2

    (2,2) = 0          (0,1) = 0        (1,2) = 1
q = [(0,1), (1,2)]

                                    (1,1) = 3   (2,2) = 0



  [3, 1, 0, 2, 1]
  [3, 1, 3, 1, 0]



                     (0,0) = 3

                     (0,3) = 2 moves = 1

                     (0,1) = 1 moves = 2

                (0,2) = 0        (1,1) = 1 moves = 3

                             (1,0) = 3     (1,2) = 3  moves = 4


                        (1,3) = 1 moves = 5

                        (1,4) = 0 moves = 6


# print the path of the shortest moves
"""

def min_moves(arr):
  q = []
  seen = set()

  q.append(((0,0), 'Start point'))
  seen.add((0,0))

  moves = -1

  # store each move's value and direction in the path list
  # print the paths if arriving at a leave node and this node is our target
  # else return nothing and keep looking for the next leave node

  while q:
    point, path = q.pop(0)
    y, x = point

    if (y == len(arr) - 1 and x == len(arr[0]) - 1):
      return {moves: path}

    possible_moves = []
    step = arr[y][x]

    # down
    if y + step < len(arr):
      possible_moves.append(((y + step, x), path + ' -> move down ' + str(step)))

    # up
    if y - step >= 0:
      possible_moves.append(((y - step, x), path + ' -> move up ' + str(step)))

    # right
    if x + step < len(arr[0]):
      possible_moves.append(((y, x + step), path + ' -> move right ' + str(step)))

    # left
    if x - step >= 0:
      possible_moves.append(((y, x - step), path + ' -> move left ' + str(step)))

    if possible_moves:
      moves += 1
    else:
      continue

    for move in possible_moves:
      if move[0] not in seen:
        seen.add(move[0])
        q.append(move)


result1 = min_moves([[2, 0, 1], [1, 3, 1], [2, 0, 0]])
print(result1)

result2 = min_moves([[3, 1, 0, 2, 1], [3, 1, 3, 1, 0]])
print(result2)

