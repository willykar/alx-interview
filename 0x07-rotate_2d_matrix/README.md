# 0x07. Rotate 2D Matrix

## Project Overview
This project is focused on implementing an in-place algorithm to rotate an `n x n` 2D matrix by 90 degrees clockwise. It challenges you to manipulate matrices and optimize your solution to operate in-place, which is a crucial aspect of efficient algorithm design.

### Key Concepts:
1. **Matrix Representation in Python:**
   - Understanding how 2D matrices are represented using lists of lists.
   - Accessing and modifying elements in a 2D matrix.

2. **In-place Operations:**
   - Performing operations on data without creating a copy of the data structure.
   - Minimizing space complexity by modifying the matrix in place.

3. **Matrix Transposition:**
   - Transposing a matrix (swapping rows and columns).
   - Implementing matrix transposition as a step in the rotation process.

4. **Reversing Rows in a Matrix:**
   - Manipulating rows of a matrix by reversing their order as part of the rotation process.

5. **Nested Loops:**
   - Using nested loops to iterate through 2D data structures like matrices.
   - Modifying elements within nested loops to achieve the desired rotation.

### Requirements
- **General**
  - Allowed editors: `vi`, `vim`, `emacs`
  - All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.10)
  - All files should end with a new line
  - The first line of all files should be exactly `#!/usr/bin/python3`
  - A `README.md` file at the root of the folder of the project is mandatory
  - Code should use the `pycodestyle` style (version 2.8.0)
  - No modules should be imported
  - All modules and functions must be documented
  - All files must be executable

### Task
#### 0. Rotate 2D Matrix
- **Description:** Given an `n x n` 2D matrix, rotate it 90 degrees clockwise.
- **Prototype:** `def rotate_2d_matrix(matrix):`
- **Requirements:**
  - Do not return anything. The matrix must be edited in-place.
  - Assume the matrix will have 2 dimensions and will not be empty.
