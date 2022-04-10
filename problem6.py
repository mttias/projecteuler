# difference between the square of the sum, and the sum of the squares

# find sum of the squares
def sumSquare(ind):
    sum = 0
    for i in range(ind+1):
        sum += i ** 2
    return sum

print(sumSquare(100))

# find square of the sum
# first: find sum
# then: find square of sum
def squareSum(ind):
    sum = 0
    for i in range(ind+1):
        sum += i
    return sum ** 2

print(squareSum(100))