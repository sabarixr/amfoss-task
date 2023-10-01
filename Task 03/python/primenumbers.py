def prime_numbers(max):
    primes = []

    for i in range(2, max + 1):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)

    return primes

def first_n_primes(n):
    if not isinstance(n, int):
        print("Error: n must be an integer")
        return []
    if n <= 0:
        print("Error: n must be greater than 0")
        return []

    return prime_numbers(n)

# Input
try:
    n = int(input("Enter the value of n: "))
except ValueError:
    print("Error: n must be an integer")
    n = 0

# Output
result = first_n_primes(n)
if result:
    print("\nPrime numbers:")
    for prime in result:
        print(prime)

