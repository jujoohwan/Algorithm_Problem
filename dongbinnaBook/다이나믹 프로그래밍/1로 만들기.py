"""
문제 : 
x가 5로 나눌어 떨어지면 5로 나눈다.
x가 3으로 나눈어 떨어지면 3으로 나눈다.
x가 2로 나누어 떨어지면 2로 나눈다.
x에서 1을 뺀다. 
"""
from sys import stdin, stdout

x = int(stdin.readline())

d = [0] * 30001

for i in range(2, x+1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i-1] + 1
    # 현재의 수가 5로 나누어 떨어질때
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5]+1)
    # 현재의 수가 3로 나누어 떨어질때
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3]+1)
    # 현재의 수가 2로 나누어 떨어질때
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2]+1)

print(d[x])
