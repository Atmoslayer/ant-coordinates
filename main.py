import argparse


def get_digit_sum(number):
    # Получаем сумму цифр в числе
    return sum(int(digit) for digit in str(abs(number)))


def check_point(x, y, condition):
    # Проверяем, удовлетворяет ли клетка условию
    return get_digit_sum(x) + get_digit_sum(y) <= condition


def count_accessible_points(start_x, start_y, condition):
    # Создаем список точек, в которые муравей смог попасть
    accepted_points = set()
    # Создаем очередь для BFS, куда сразу попадает стартовая точка
    queue = [(start_x, start_y)]

    while queue:
        # Сразу удаляем из очереди точку, которую проверяем
        x, y = queue.pop(0)
        # Выполняем проверку точки по заданному условию
        if (x, y) not in accepted_points and check_point(x, y, condition):
            # В случае прохождения проверки добавляем точку в список, если ещё этого не сделали
            accepted_points.add((x, y))

            # Находим все точки, в радиусе единицы от исследуемой позиции и добавляем их в очередь
            neighboring_points = [(x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)]
            queue.extend(neighboring_points)

    return len(accepted_points)


def main():
    # Принимаем и обрабатываем аргументы для работы скрипта
    parser = argparse.ArgumentParser(description='Start points parser')
    parser.add_argument('--x', help='Enter start x coordinate', type=int, default=1000)
    parser.add_argument('--y', help='Enter start y coordinate', type=int, default=1000)
    parser.add_argument('--condition', help='Enter validation condition', type=int, default=25)
    arguments = parser.parse_args()
    accessible_points_quantity = count_accessible_points(arguments.x, arguments.y, arguments.condition)
    print(f'Количество точек, доступных для посещения: {accessible_points_quantity}')


if __name__ == '__main__':
    main()
