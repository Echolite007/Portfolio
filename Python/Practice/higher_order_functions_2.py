def divisor(x):
    def dividend(y):
        return x / y
    return dividend 

divide = divisor(10)
print(divide(2))