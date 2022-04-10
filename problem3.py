# försök 1

number = 600851475143
primes = []
primesDiv = []

# first find all the primes up to that number
def isPrime(x):
    primeYes = 1
    for y in range(x-2):
        if x % (y + 2) == 0:
            primeYes = 0
    if primeYes == 1 and x != 0 and x != 1: 
        primes.append(x)

for num in range(number):
    isPrime(num)

# divide w/ primes to find factor primes
for x in range(len(primes)-1):
    if number % (primes[x]) == 0:
        primesDiv.append((primes[x]))

print(primesDiv)

# print(primes[-2])