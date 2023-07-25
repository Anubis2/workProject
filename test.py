while True:
    try:
        number1 = input("Введите первое число: ")
        number2 = input("Введите второе число: ")
        sum = float(number1) + float(number2)
        if sum.is_integer():
            sum = int(sum)
        print(f"Сумма введенных чисел: {sum}")
        break
    except ValueError:
        print("Введите целые числа!!")



name = input("What is your name? ")
age = input("Your age is: ")
print(f"Name: {name}, Age: {age}")


def average(a, b, c):
    list = [a, b, c]
    result = (a + b + c) / len(list)
    return result


print(average(1, 2, 3))