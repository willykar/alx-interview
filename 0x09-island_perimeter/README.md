# 0x09. Island Perimeter

## Description

This project involves calculating the perimeter of an island within a grid. The grid is represented by a 2D list of integers where:
- `0` represents water.
- `1` represents land.

The function `island_perimeter(grid)` will return the perimeter of the island described in the grid. The island is completely surrounded by water, there is only one island (or none), and the island doesn’t have lakes (water inside that isn’t connected to the water surrounding the island).

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the project is mandatory
- Code should use the PEP 8 style (version 1.7)
- No module imports are allowed
- All modules and functions must be documented
- All files must be executable

## Function Prototype

```Python
def island_perimeter(grid):
    """Calculate the perimeter of an island in a grid."""
```

Parameters:
grid: 
A list of lists of integers where 0 represents water and 1 represents land.

Returns:
The perimeter of the island.
