from random import choice


class RandomWalk():
    """Класс для генерирования случайных блужданий."""

    def __init__(self, num_point=5000):
        """Инициализирует атрибуты блуждания"""
        self.num_point = num_point

        # Все блуждания начинаются с точки (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Вычисляет все точки блуждания"""

        # Шаги генерируются до достижения нужной длины
        while len(self.x_values) < self.num_point:
            x_step = self.get_step()
            y_step = self.get_step()

            # Отклонение нулевых перемещений
            if x_step == 0 and y_step == 0:
                continue

            # Вычисление следующих значений х и у
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self):

        # Определение направления и длины перемещения    
            direction = choice([1, -1])
            distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
            step = direction * distance
            return step