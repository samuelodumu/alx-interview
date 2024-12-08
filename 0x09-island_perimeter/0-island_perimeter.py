#!/usr/bin/python3
"""contains `island_perimeter` function"""


def island_perimeter(grid):
    """calculates and returns the perimeter of a single island in a grid"""
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # check if cell is in land
            if grid[i][j] == 1:
                # assuming all 4 sides of the land cell are exposed,
                # check the top (i-1, j)
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # check the bottom (i+1, j)
                if i == len(grid) - 1 or grid[i+1][j] == 0:
                    perimeter += 1
                # check the left (i, j-1)
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # check the right (i, j+1)
                if j == len(grid[i]) - 1 or grid[i][j+1] == 0:
                    perimeter += 1
    return perimeter
