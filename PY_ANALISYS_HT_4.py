# У вас есть список строк, где каждая строка представляет собой текст.
# Напишите функцию count_words, которая возвращает общее количество слов
# во всех строках. Используйте list comprehensions.

def count_words(texts):
    return sum(len(text.split()) for text in texts)


texts = ["Hello world", "Python is great", "I love coding"]
print(count_words(texts))
