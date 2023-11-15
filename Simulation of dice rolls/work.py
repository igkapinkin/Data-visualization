# 15.6. Два кубика D8: создайте модель, которая показывает,
# что происходит при 1000-кратном бросании двух восьмигранных кубиков.

from die import Die
from plotly import offline
from plotly.graph_objs import Bar, Layout

# die_1 = Die(8)
# die_2 = Die(8)

# results = []
# for result in range(1000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)

# frequencies = []
# max_result = die_1.num_sides + die_2.num_sides
# for value in range(2, max_result+1):
#     frequency = results.count(value)
#     frequencies.append(frequency)

# x_values = list(range(2, max_result+1))
# data = [Bar(x=x_values, y=frequencies)]

# x_axis_config = {"title": "Result", "dtick": 1}
# y_axis_config = {"title": "Frequency of Result"}
# my_layout = Layout(title="Results of rolling a D8 and a D8 1000 times",
#                    xaxis=x_axis_config, yaxis=y_axis_config)
# offline.plot({"data": data, "layout": my_layout}, filename="d8_d8.html")


# 15.7. Три кубика: при броске трех кубиков D6 наименьший возможный результат равен 
# 3, а наибольший — 18. Создайте визуализацию, которая показывает, что происходит при 
# броске трех кубиков D6

# die_1 = Die(6)
# die_2 = Die(6)
# die_3 = Die(6)

# results = []
# for result in range(1000):
#     result = die_1.roll() + die_2.roll() + die_3.roll()
#     results.append(result)

# frequencies = []
# max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
# for value in range(3, max_result+1):
#     frequency = results.count(value)
#     frequencies.append(frequency)

# x_values = list(range(3, max_result+1))
# data = [Bar(x=x_values, y=frequencies)]

# x_axis_config = {"title": "Result", "dtick": 1}
# y_axis_config = {"title": "Frequency of Result"}
# my_layout = Layout(title="Results of rolling three D6 1000 times",
#                    xaxis=x_axis_config, yaxis=y_axis_config)
# offline.plot({"data": data, "layout": my_layout}, filename="d6_d6_d6.html")


# 15.8. Умножение: при броске двух кубиков результат обычно определяется суммированием двух чисел.
# Создайте визуализацию, которая показывает, что происходит при умножении этих чисел.

die_1 = Die(8)
die_2 = Die(8)

results = [die_1.roll() * die_2.roll() for _ in range(1000)]
# for result in range(1000):
#     result = die_1.roll() * die_2.roll()
#     results.append(result)

frequencies = [results.count(value) for value in range(2, die_1.num_sides * die_2.num_sides+1)]
# max_result = die_1.num_sides * die_2.num_sides
# for value in range(2, max_result+1):
#     frequency = results.count(value)
#     frequencies.append(frequency)

x_values = list(range(2, die_1.num_sides * die_2.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "Result", "dtick": 1}
y_axis_config = {"title": "Frequency of Result"}
my_layout = Layout(title="Results of rolling two D8 1000 times",
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({"data": data, "layout": my_layout}, filename="d8_d8.html")


# 15.9. Генераторы: для наглядности в списках этого раздела используется длинная форма 
# цикла for. Если вы уверенно работаете с генераторами списков,
# попробуйте написать генератор для одного или обоих циклов в каждой из этих программ