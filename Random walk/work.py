# 15.3. Молекулярное движение: измените программу rw_visual.py и замените plt.scatter()
# вызовом plt.plot(). Чтобы смоделировать путь пыльцевого зерна на поверхности водяной капли,
# передайте значения rw.x_values и rw.y_values и включите аргумент linewidth. 
# Используйте 5000 точек вместо 50 000

import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Новые блуждания стрятся до тех пор, пока программа остается активной
while True:
    # Постороение случайного блуждания
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Нанесение точек на диаграмму
    plt.style.use("classic")
    fig, ax = plt.subplots(figsize=(15, 9))
    points_number = range(rw.num_point)

    ax.plot(rw.x_values, rw.y_values, linewidth=3)
    
    # Выделение первой и последней точек
    ax.scatter(0, 0, c="green", edgecolors="none", s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c="blue", edgecolors="none",
               s=100)
    
    # Удаление осей
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_runnung = input("Make anoyger walk? (y/n): ")
    if keep_runnung == "n":
        break