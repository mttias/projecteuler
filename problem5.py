# 2520 is the smallest number that can be divided by each of
# the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible
# by all of the numbers from 1 to 20?

answer = 9699690
points = 0
correctAnswer = 0

while points != 20:
    print("Points", points)
    # print("Answer", answer)
    points = 0
    answer -= 10
    for x in range(1,21,1):
        if answer % x == 0:
            points += 1
    if points == 20:
        correctAnswer = answer
        break

print(correctAnswer)
