def greet():
    print("Hello Python")
    print("first function in python")


greet()


# function with single parameter
def greet_with_name(name):
    print("Hello ", name)
    print("welcome to python world")


greet_with_name("Hemanth")


# function with 2 parameters
def add_numbers(n1, n2):
    result = n1 + n2
    print("Sum of numbers is -> ", result)


add_numbers(10,20.1)


# function with return value
def sum_of_numbers(n1, n2):
    number_sum = n1 + n2
    return number_sum


result = sum_of_numbers(23, 24)
print("Sum of 2 numbers ", result)


