import math

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

print(f"Число 7 простое? {is_prime(7)}")
print(f"Число 10 простое? {is_prime(10)}")