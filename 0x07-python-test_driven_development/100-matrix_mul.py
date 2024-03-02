#!/usr/bin/python3
"""multiplying a matrix"""


def matrix_mul(m_a, m_b):
    """Multiply Matrix"""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for line in m_b:
        if not isinstance(line, list):
            raise TypeError("m_b must be a list of lists")
        if len(line) != len(m_b[0]):
            raise TypeError("each row of m_a must be of the same size")
        for j in line:
            if not isinstance(j, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    if m_b == [] or m_b == [[]]:
        raise ValueError("m_a can't be empty")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    mul = []
    for x in range(len(m_a)):
        result = []
        for y in range(len(m_b[0])):
            display = 0
            for w in range(len(m_b)):
                display += m_a[x][w] * m_b[w][y]
            result.append(display)
        mul.append(result)
    return mul


