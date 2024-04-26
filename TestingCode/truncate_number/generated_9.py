import math

def truncate_number(number: float) -> float: 
    """ Given a positive floating point number, it can be decomposed into and integer part (largest integer smaller than given number) and decimals (leftover part always smaller than 1). Return the decimal part of the number. >>> truncate_number(3.5) 0.5 """ 
    return number - math.trunc(number) 


def is_prime(number: int) -> bool: 
    """ Given a positive integer, check if it is a prime number. """ 
    if number == 2: 
        return True 
    if number % 2 == 0 or number <= 1: 
        return False 
    for i in range(3, int(math.sqrt(number)) + 1, 2): 
        if number % i == 0: 
            return False 
    return True 


def is_perfect_square(number: int) -> bool: 
    """ Given a positive integer, check if it is a perfect square. """ 
    return math.sqrt(number).is_integer() 


def is_power_of_two(number: int) -> bool: 
    """ Given a positive integer, check if it is a power of two. """ 
    return number!= 0 and ((number & (number - 1)) == 0) 


def is_palindrome(number: int) -> bool: 
    """ Given a positive integer, check if it is a palindrome. """ 
    return str(number) == str(number)[::-1] 


def is_abundant(number: int) -> bool: 
    """ Given a positive integer, check if it is an abundant number. """ 
    return sum_of_divisors(number) > number 


def is_deficient(number: int) -> bool: 
    """ Given a positive integer, check if it is a deficient number. """ 
    return sum_of_divisors(number) < number 


def is_amicable(number: int) -> bool: 
    """ Given a positive integer, check if it is an amicable number. """ 
    return sum_of_divisors(number) == sum_of_divisors(sum_of_divisors(number)) and number!= sum_of_divisors(number) 


def is_circular_prime(number: int) -> bool: 
    """ Given a positive integer, check if it is a circular prime. """ 
    return is_prime(number) and is_circular(number) 


def is_circular(number: int) -> bool:
    """ Given a positive integer, check if it is a circular number. """ 
    return str(number) == str(number)[::-1] 


def is_neon_number(number: int) -> bool: 
    """ Given a positive integer, check if it is a neon number. """ 
    return sum_of_digits(number) == sum_of_digits(sum_of_digits(number)) 


def is_narcissistic(number: int) -> bool: 
    """ Given a positive integer, check if it is a narcissistic number. """ 
    return sum_of_digits(number) == sum_of_digits(sum_of_digits(number)) == sum_of_digits(sum_of_digits(sum_of_digits(number))) 


def is_automorphic(number: int) -> bool: 
    """ Given a positive integer, check if it is an automorphic number. """ 
    return sum_of_digits(number) == sum_of_digits(sum_of_digits(number)) 


def is_polygonal(number: int) -> bool: 
    """ Given a positive integer, check if it is a polygonal number. """ 
    return sum_of_digits(number) == sum_of_digits(sum_of_digits(number)) == sum_of_digits(sum_of_digits(sum_of_digits(number))) 