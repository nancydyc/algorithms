def maxAreaofIsland(grid):
    """
    For example:
    >>> maxAreaofIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]])
    4
    """
    def explore_island_area(r, c) :
        print(f'row {r} col {c}')
        if r >= len(grid) or r < 0 or c >= len(grid[0]) or c < 0 or grid[r][c] != 1:
            # print('area so far', area)
            return 0

        if grid[r][c] == 1:
            # area += 1
            # print('Current island area increase to:', area)
            grid[r][c] = 7

        return 1                            \
            + explore_island_area(r, c + 1) \
            + explore_island_area(r + 1, c) \
            + explore_island_area(r, c - 1) \
            + explore_island_area(r - 1, c)

    max_area = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # print(f'island {row}-{col}')
            if grid[row][col] == 1:
                # area = 0
                current_island_area = explore_island_area(row, col)
                # print('Current island area is', current_island_area)
                if current_island_area >= max_area:
                    max_area = current_island_area
                # print('Max area is', max_area)
            # print('----------------------------------------------')
        # print('========================================================')
    return max_area

############################################################################
if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU DID AN EXCELLENT JOB!\n")
