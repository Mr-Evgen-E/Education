import numpy

# Для работы нужен модуль numpy (для округления всех элементов списка до
# второго знака (копейки)
money = input("Введите сумму вклада: ")
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

# Выбран тип float, так как при введении суммы с копейками при int (через точку)
# приложение "падает"
percent_a = float(money) / 100 * per_cent.get('ТКБ')
percent_b = float(money) / 100 * per_cent.get('СКБ')
percent_c = float(money) / 100 * per_cent.get('ВТБ')
percent_d = float(money) / 100 * per_cent.get('СБЕР')

deposit = numpy.around(list([percent_a, percent_b, percent_c, percent_d]), decimals=2)
print(deposit)

print("Максимальная сумма, которую вы можете заработать:", max(deposit))
