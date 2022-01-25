userInput = int(input())
userIndex = [0 for i in range(24)]
userArray = list(map(int, input().split())) 

for i in range(userInput):
    userIndex[userArray[i]] += 1

for i in range(1,24):
    print(userIndex[i], end=' ')
