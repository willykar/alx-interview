# 0x0A. Prime Game

## Description

This project involves determining the winner of a game where two players, Maria and Ben, take turns selecting prime numbers from a set of consecutive integers. When a player selects a prime number, they remove it and all its multiples from the set. The game ends when no more moves are possible, and the player who cannot make a move loses. The project requires efficient handling of prime numbers, game logic, and strategic decision-making to determine the winner.

The challenge covers important concepts such as:
- Prime Numbers
- Sieve of Eratosthenes
- Game Theory
- Dynamic Programming / Memoization
- Python Programming

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- Code must adhere to the PEP 8 style (version 1.7.x)
- All files must be executable
- A `README.md` file is mandatory at the root of the project folder

## Usage

### Prototype

```python
def isWinner(x, nums)
```
x: Number of rounds
nums: Array of integers representing the set size for each round
The function should return the name of the player with the most wins or None if it's a tie.
