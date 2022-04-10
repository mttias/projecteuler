d = ""
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

for x in range(1,1000000):
    d += str(x)

print(int(d[1])*int(d[10])*int(d[100])*int(d[1000])*int(d[10000])*int(d[100000])*int(d[1000000]))