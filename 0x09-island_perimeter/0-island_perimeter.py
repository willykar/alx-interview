#!/usr/bin/python3
"""island_perimeter"""


def island_perimeter(grid):
    """Calculate the perimeter of an island in a grid."""
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check all four sides
                if i == 0 or grid[i-1][j] == 0:  # Top side
                    perimeter += 1
                if i == rows-1 or grid[i+1][j] == 0:  # Bottom side
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:  # Left side
                    perimeter += 1
                if j == cols-1 or grid[i][j+1] == 0:  # Right side
                    perimeter += 1
    
    return perimeter
