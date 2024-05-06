#!/usr/bin/env python3

from utils import input_matrix, print_matrix
from jordan import invert

# Get input
matrix = input_matrix()

# Invert the matrix
#                             Simply ignore the exception
rank, matrix = invert(matrix, error_handler=lambda e: None)

print_matrix(matrix, "Resulting matrix:")

print("Matrix rank:", rank)