n = int(input())

for i in range(n, 0, -1):
    temp = 2 * i - 1
    print((' ' * (n-i)) + ('*'*temp))

for i in range(2, n+1):
    temp = 2 * i - 1
    print((' ' * (n-i) + ('*'*temp)))
