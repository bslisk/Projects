# Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.

def fibonacci_to_nth(n: int) -> str:
    number_one = 0
    number_two = 1
    fibonacci = '1'
    for _ in range(n-1):
        result = number_one + number_two
        fibonacci += ', ' + str(result)
        number_one = number_two
        number_two = result

    return fibonacci


def fibonacci_to_number(num: int) -> str:
    number_one = 0
    number_two = 1
    fibonacci = '1'
    while number_one + number_two <= num:
        result = number_one + number_two
        fibonacci += ', ' + str(result)
        number_one = number_two
        number_two = result

    return fibonacci


print('Fibonacci sequence to the 12th term:')
print(fibonacci_to_nth(12))

print('Fibonacci sequence to number 55:')
print(fibonacci_to_number(55))
