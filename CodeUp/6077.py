result = int(input())

temp = 0
for i in range(1, result+1):
    if(i % 2 == 0):
        temp += i

print(temp)