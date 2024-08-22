
# 0x08. Making Change

## Project Overview
This project tackles the classic problem of finding the minimum number of coins required to make up a given total amount. It challenges you to apply your understanding of algorithms, particularly greedy algorithms and dynamic programming, to devise an efficient solution.

## Key Concepts

- **Greedy Algorithms**:
  - Used to make a series of choices, each of which looks best at the moment.
  - Might not always provide the optimal solution for the coin change problem, depending on the coin denominations.

- **Dynamic Programming**:
  - A method for solving complex problems by breaking them down into simpler subproblems.
  - Useful for the coin change problem, especially when a greedy approach fails to find the optimal solution.

- **Algorithmic Complexity**:
  - Understanding and analyzing the time and space complexity of your solution is crucial.
  - Strive for a solution with lower complexity to meet runtime constraints.

## Requirements

- **General**:
  - Allowed editors: `vi`, `vim`, `emacs`
  - All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
  - All files should end with a new line
  - The first line of all files should be exactly `#!/usr/bin/python3`
  - A `README.md` file, at the root of the folder of the project, is mandatory
  - Your code should use the PEP 8 style (version 1.7.x)
  - All files must be executable

## Task

### 0. Change comes from within

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

- **Prototype**: `def makeChange(coins, total):`
- **Parameters**:
  - `coins`: A list of integers representing the values of available coins.
  - `total`: An integer representing the target amount.
- **Return**:
  - The fewest number of coins needed to meet the `total`.
  - Return `0` if `total` is `0` or less.
  - Return `-1` if the total cannot be met with the given coins.

#### Example:
```python
makeChange([1, 2, 25], 37)  # Output: 7
makeChange([1256, 54, 48, 16, 102], 1453)  # Output: -1
