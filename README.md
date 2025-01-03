# l_systems
Напишите программу с графическим пользовательским интерфейсом на PyQT, которая умеет по заданному определению строить L-системы. Определение L-системы задается в текстовом файле, который необходимо открыть с помощью диалога открытия файла при запуске программы. Структура файла следующая:

Первая строка — название системы (строка); Вторая строка — целое число, говорящее о том, на сколько углов делится плоскость. Этот параметр необходим для организации поворотов; Третья строка — аксиома; Остальное — теоремы.
Пример:

Кривая Коха

5
F
F F-F++F-F

Первый шаг эволюции строится автоматически, затем возможно перемещение между шагами эволюции с помощью слайдера.

Первую линию начинайте строить из точки с координатами (250, 400)

Также, установите длину линий равной 20 пикселям

Класс, реализующий окно приложения, назовите LSystem.

Цвет, которым будете рисовать сохраните в атрибут color объекта приложения при инициализации.
