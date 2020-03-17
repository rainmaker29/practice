# A way to find out prime numbers upto given number efficiently

primes[2]


def isPrime(n):
    for i in range(2,int(0.5**2)+1):
        if not n%i:
            return False
    return True

def whatever_function_the_program_requires(n):
    biggest_prime=primes[-1]
    if n>biggest_prime:
        for i in range(biggest_prime+1,n+1):
            if isPrime(i):
                primes.append(i)

    return #dummy return 
