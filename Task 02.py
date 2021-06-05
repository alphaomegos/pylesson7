# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
#   для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
#   реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

class Fabric:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_o(self):
        return round(self.width / 6.5 + 0.5)

    def get_square_c(self):
        return round(self.height * 2 + 0.3)

    @property
    def get_sq_full(self):
        return str(f'Total fabric surface >>> '
                   f' {round((self.width / 6.5 + 0.5) + (self.height * 2 + 0.3))}')


class Overcoat(Fabric):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Overcoat fabric >>> {self.square_c}'


class Costume(Fabric):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_j = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Costume fabric >>>  {self.square_j}'

coat = Overcoat(2, 5)
jacket = Costume(3, 4)

print(coat)
print(jacket)
print(coat.get_sq_full)
print(jacket.get_sq_full)
print(jacket.get_square_o())
print(jacket.get_square_c())