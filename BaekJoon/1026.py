from sys import stdin, stdout

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
b = list(map(int, stdin.readline().split()))

answer = 0

for i in range(n):
    answer += max(a) * min(b)
    a.pop(a.index(max(a)))
    b.pop(b.index(min(b)))
print(answer)
