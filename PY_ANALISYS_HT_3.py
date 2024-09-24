# Напишите функцию calc_income_by_year, которая принимает список с
# датами и список с выручкой, а возвращает словарь, где ключи — это года, а
# значения — это выручка за соответствующие года. Используйте аннотирование
# типов.
# Пример:
# print(calc_income_by_year(['2021-11-01', '2021-12-15', '2020-11-30'], [100, 200,
# 150]))
# На выходе: {'2021': 300, '2020': 150}


def calc_income_by_year(dates: int, incomes=0, ) -> dict:
    years = [dates[i][0:4] for i in range(len(dates))]
    return {key: sum(inc for k, inc in zip(years, incomes) if k == key) for key in sorted(set(years))}


print(calc_income_by_year(['2021-11-01', '2021-12-15', '2020-11-30'], [100, 200, 150]))
