#!/usr/bin/python3
"""
Define `rotate_2d_matrix` function
"""


def rotate_2d_matrix(matrix):
    """Rotates `matrix` 90 degree clockwise in place."""
    matrix.reverse()
    # reflect the elements above main diagonal about it
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j > i:
                # swap matrix[i][j] with matrix[j][i]
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
