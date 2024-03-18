a = int(input())
temp = 1
for i in range(a-1, -1, -1):
    print((' '*i) + (('*')*temp))
    temp += 1
