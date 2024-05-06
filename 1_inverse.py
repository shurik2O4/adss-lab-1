#!/usr/bin/env python3

from utils import input_matrix, print_matrix
from jordan import invert

# Get input
matrix = input_matrix()

# Square matrix?
if matrix.shape[0] != matrix.shape[1]:
    raise ValueError("Matrix must be square")

# Invert the matrix
_, matrix = invert(matrix)

print_matrix(matrix, "Inverse matrix:")