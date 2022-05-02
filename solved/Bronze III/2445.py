n = int(input())
temp = n * 2
for i in range(1, n+1):
    temp -= 2
    print(('*'*i) + (' ' * temp) + ('*' * i))


temp = 2
for j in range(n-1, 0, -1):
    print(('*'*j) + (' ' * temp) + ('*'*j))
    temp += 2
