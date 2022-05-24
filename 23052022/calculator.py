def addition(*args: float) -> float:
    total = 0
    for i in args:
        total += i
    return total


def subtraction(a: float, b: float) -> float:
    return a-b


def multiplication(a: float, b: float) -> float:
    return a-b


def division(a: int, b: int) -> float:
    return a/b


def power(a: int, b: int) -> int:
    return a**b


print(addition(2,3,4,5))
print(subtraction(5,6))
print(multiplication(5,7))
print(division(15,3))
print(power(3,2))





