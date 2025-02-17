#!/usr/bin/python3
"""perimeter of the island described in the grid."""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Args:
        grid (list of list of int): 2D grid where 0
        represents water and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
