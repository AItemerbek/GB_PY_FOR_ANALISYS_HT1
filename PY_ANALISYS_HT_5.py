# У вас есть список сотрудников, где каждый сотрудник представлен кортежем из
# имени и возраста. Напишите функцию average_age, которая находит и
# возвращает средний возраст сотрудников, исключая тех, чей возраст меньше
# нуля (ошибочные данные).

employees = [("Alice", 30), ("Bob", -5), ("Charlie", 40)]


def average_age(employees):
    valid_ages = [age for name, age in employees if age >= 0]
    return sum(valid_ages) / len(valid_ages) if valid_ages else 0


employees = [("Alice", 30), ("Bob", -5), ("Charlie", 40)]
print(average_age(employees))
