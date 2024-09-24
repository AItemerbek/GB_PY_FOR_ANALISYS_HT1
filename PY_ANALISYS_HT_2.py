# Вам дан список покупок, где каждый элемент — это название продукта.
# Напишите функцию unique_products_count, которая возвращает
# количество уникальных продуктов в списке.

def unique_products_count(units):
    return len(set(units))


products = ['apple', 'banana', 'apple', 'orange', 'banana', 'grape']
print(unique_products_count(products))
