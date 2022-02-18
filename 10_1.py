from itertools import zip_longest


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n'.join(['\t'.join([str(i) for i in line]) for line in self.matrix]))

    def __add__(self, other):
        my_el = (map(sum, zip_longest(*el, fillvalue=0)) for el in zip_longest(self.matrix, other.matrix, fillvalue=[]))
        return Matrix(my_el)


m = [[1, 2, 3], [3, 4, 5], [5, 6, 7], [4, 5]]
n = [[2, 3, 4], [5, 5, 5], [-5, -4, -3]]

m_1 = Matrix(m)
m_2 = Matrix(n)

print(m_1, '\n')
print(m_2, '\n')
print(m_1 + m_2)
