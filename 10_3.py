class Cell:
    def __init__(self, cell):
        self.cell = cell
        self.symbol = '*'

    def make_order(self, rows):
        return '\n'.join([self.symbol * rows for _ in range(self.cell // rows)]) \
               + '\n' + self.symbol * (self.cell % rows)

    def __str__(self):
        return f'{self.cell}'

    def __sub__(self, other):
        print('Вычитание ячеек: ')
        return Cell(self.cell - other.cell) if self.cell - other.cell > 0 \
            else 'Вычитание не возможно! Ячеек в первой клетке меньше, чем во второй.'

    def __mul__(self, other):
        print('Умножение ячеек: ')
        return Cell(self.cell * other.cell)

    def __add__(self, other):
        print('Сумма ячеек: ')
        return Cell(self.cell + other.cell)

    def __floordiv__(self, other):
        print('Деление ячеек без остатка: ')
        return Cell(self.cell // other.cell)


a = Cell(15)
b = Cell(24)

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(b.make_order(5))
