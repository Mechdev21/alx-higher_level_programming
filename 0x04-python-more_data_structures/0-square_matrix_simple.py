#!/usr/bin/python3

# python program that:
# computes the square value of all integers of a matrix.

def square_matrix_simple(matrix=[]):
    new_matrix = [[value ** 2 for value in row]for row in matrix]
    return new_matrix
