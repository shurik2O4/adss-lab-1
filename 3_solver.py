#!/usr/bin/env python3

from utils import input_matrix, print_matrix
from jordan import invert

# Get input
matrix = input_matrix("Equation matrix:")

# Separate the values vector
constants, matrix = matrix[:, -1], matrix[:, :-1]

# Square matrix?
if matrix.shape[0] != matrix.shape[1]:
    raise ValueError("Matrix must be square")

# Invert the matrix
_, matrix = invert(matrix)

# Xi = [Inverse matrix] * [Constants]
result = matrix @ constants

print_matrix(matrix, "Inverse matrix:")

# Print the result
print(f"Result: {result}")