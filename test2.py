def average(*numbers):
    result = sum(numbers)
    total = result / len(numbers)
    return total


print(average(5, 6, 6))
