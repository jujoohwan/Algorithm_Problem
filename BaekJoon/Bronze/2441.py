n = int(input())
temp = n
for i in range(n):
    print((' '*i) + ("*"*temp))
    temp -= 1
