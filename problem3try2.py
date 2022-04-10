# försök 2

number = 600851475143
primeFactor = 0

for x in range(2, 500, 1):
    if number % x == 0:
        primeFactor = number / x
        break

print(primeFactor)

# answer 1
# 8462696833