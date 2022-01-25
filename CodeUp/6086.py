result = int(input())

temp = 0
for i in range(1,100000000):
    temp += i
    if (result <= temp):
        print(temp)
        break
