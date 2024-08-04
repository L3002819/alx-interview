#!/usr/bin/python3
"""Define islandPerimeter function."""


def island_perimeter(grid: list) -> int:
    """Retrun the perimeter of the island represented by `grid`."""
    perimeter = 0
    height = len(grid)
    width = len(grid[0])  # grid is rectangular, same width for each row
    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:  # if land cell
                perimeter += 4
                # check the left cell
                if i > 0 and grid[i - 1][j] == 1:
                    # then there is two edges common in between
                    perimeter -= 2
                # check the above cell
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
