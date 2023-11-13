# УПРАЖНЕНИЯ
# 15.1. Кубы: число, возведенное в третью степень, называется «кубом».
# Нанесите на диаграмму первые пять кубов, а затем первые 5000 кубов.
# 15.2. Цветные кубы: примените цветовую карту к диаграмме с кубами.

import matplotlib.pyplot as plt

# 15.1
x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.style.use("ggplot")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Values", fontsize=14)

ax.tick_params(axis="both", which="major", labelsize=14)

ax.axis([0, 5500, 0, 5500000])

plt.show()

# 15.2
x_values = list(range(1, 6))
y_values = [x**3 for x in x_values]

plt.style.use("ggplot")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Values", fontsize=14)

ax.tick_params(axis="both", which="major", labelsize=14)

plt.show()

# Дополнителный вариант решения

# Создаем списки значений для x и y
x_values_5 = list(range(1, 5001))
y_values_5 = [x**3 for x in x_values_5]

x_values_5000 = list(range(1, 50))
y_values_5000 = [x**3 for x in x_values_5000]

plt.style.use("ggplot")

# Создаем фигуру и оси
fig, ax = plt.subplots()

# Рисуем первые пять кубов
ax.scatter(x_values_5, y_values_5, c=y_values_5, cmap=plt.cm.Blues, s=25, label="First 5 Cubes")

# Рисуем первые 5000 кубов
ax.scatter(x_values_5000, y_values_5000, c=y_values_5000, cmap=plt.cm.Reds, s=10, label="First 5000 Cubes")

# Устанавливаем заголовок и метки осей
ax.set_title("Cubes", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Values", fontsize=14)

# Устанавливаем размер меток на осях
ax.tick_params(axis="both", which="major", labelsize=14)

# Добавляем легенду
ax.legend()

# Показываем диаграмму
plt.show()