import math

def is_prime(n):
    """
    Check if a number is a prime number.

    A prime number is only divisible by 1 and itself.
    """
    if n <= 1:  # 0 and 1 are not prime numbers
        return False
    if n == 2:  # 2 is the only even prime number
        return True
    if n % 2 == 0:  # Exclude other even numbers
        return False
    # Check divisors up to the square root of n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

try:
    n = int(input("Enter a number to check if it's a prime number: "))
    if is_prime(n):
        print(f"The number {n} is a prime number.")
    else:
        print(f"The number {n} is not a prime number.")
except ValueError:
    print("Invalid input! Please enter a valid integer.")
