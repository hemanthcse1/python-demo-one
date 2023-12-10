def add_numbers(n1, n2):
    addition = n1 + n2
    return addition


def sub_numbers(n1, n2):
    subtraction = n1 - n2
    return subtraction


def multiplication_numbers(n1, n2):
    multiplication = n1 * n2
    return multiplication


def division_numbers(n1, n2):
    division = n1 / n2
    return division


addition_result = add_numbers(10, 20)
print("Sum of numbers: ", addition_result)

subtraction_result = sub_numbers(20, 10)
print("Subtraction of numbers: ", subtraction_result)

multiplication_result = multiplication_numbers(5, 2)
print("Multiplication of numbers: ", multiplication_result)

division_result = division_numbers(20, 5)
print("Division of numbers: ", division_result)
