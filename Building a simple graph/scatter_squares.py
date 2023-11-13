# Нанесение и оформление отдельных точек функцией scatter()

import matplotlib.pyplot as plt

# Вывод серии точек функцией scatter()
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

# Автоматическое вычисление данных
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.style.use("grayscale")
fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, s=200)
# ax.scatter(x_values, y_values, c="blue", s=10) просто выбор цвета

# Цветовыек карты
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

#  возможно определять пользовательские цвета в цветовой модели RGB. Чтобы определить цвет,
#  передайте аргумент c с кортежем из трех дробных значени
#  ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)

# Назначение заголовка диаграммы и меток осей
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Назначение размера шрифта делений на осях
ax.tick_params(axis="both", which="major", labelsize=14)

# Назначение диапазона для каждой оси
ax.axis([0, 1100, 0, 110000])

plt.show()

# Автоматическое сохранение диаграмм
# Если вы хотите, чтобы программа автоматически сохраняла диаграмму в файле, 
# замените вызов plt.show() вызовом plt.savefig():

# plt.savefig('squares_plot.png', bbox_inches='tight')