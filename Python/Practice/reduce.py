import functools

numbers = [10, 20, 0.5, 50]
product_numbers = functools.reduce(lambda x, y: x * y, numbers)
print(product_numbers)