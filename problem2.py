# STATUS: 200 OK

fibonacci = [1, 1]
sum = 0

while fibonacci[-1] < 4000000:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
    if fibonacci[-1] % 2 == 0:
        sum += fibonacci[-1]

print(sum)