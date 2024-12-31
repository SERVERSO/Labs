
def greet(name):
    print(f"Привет, {name}")
greet(input("Введите имя: "))


def square(num):
    return num**2
print(square(int(input("Введите число: "))))

def max_of_two(x, y):
    return max(x, y)
print(f" Большее число между x, y: {max_of_two(int(input("Введите первое число: ")), int(input("Введите второе число: ")))}")


def describe_person(name, age=30):
    print(f"Человека зовут {name}. Ему {age} лет")
describe_person(input("Введите имя человека: "))

def is_prime(number):
    _is = True
    for x in range(2, int(number**0.5)):
        if number % x == 0:
            print(f"Первый попавшийся делитель: {x} ")
            _is = False
            break
    return _is

print(is_prime(int(input("Введите число: "))))
