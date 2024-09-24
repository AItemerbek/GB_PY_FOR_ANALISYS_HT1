# Задание 1. Нормализация оценок студентов
# Вам дан список оценок студентов, в котором некоторые оценки могут быть
# недействительными (отрицательные числа). Напишите функцию
# normalize_grades, которая удаляет недействительные оценки и возвращает
# список всех оставшихся оценок, отсортированных в порядке убывания.

grades = [95, -10, 82, 90, -5, 77]


def normalize_grades(array):
    return sorted([i for i in array if i > 0], reverse=True)


print(normalize_grades(grades))