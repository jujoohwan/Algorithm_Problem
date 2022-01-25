result = int(input())
userArray = list(map(int, input().split()))

for i in range(result-1,-1, -1):
    print(userArray[i],end=' ')