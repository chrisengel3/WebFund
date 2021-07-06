for x in range(151):
    print(x)

for x in range(5,1001,5):
    print(x)

for x in range(1,101):
    if x%10 == 0:
        print("coding dojo")
    elif x%5 == 0:
        print("coding")    
    else: print(x)


sum = 0
for i in range(500000):
    if i%2 != 0:
        sum = sum + i

print(sum)

for i in range(2018, 1, -4):
    print(i)

lowNum = 2
highNum = 20
multi = 3
for i in range(lowNum, highNum, multi):
    print(i)

