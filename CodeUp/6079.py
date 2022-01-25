result = int(input())

temp = 1
addTemp = 0
for i in range(1,1000):
    addTemp += i
    temp = i
    if(addTemp >= result):
        break
print(temp)