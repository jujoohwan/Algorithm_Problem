from sys import stdin, stdout
from collections import deque, defaultdict
input = stdin.readline

"""
a -> b 최소 몇번?
"""


def bfs(a, b, data, n):
    queue = deque()
    queue.append(a-1)
    check = [-1]*n
    check[a-1] = 0
    while queue:
        popdata = queue.popleft()
        for i in range(n):
            if (i-popdata) % data[popdata] == 0 and check[i] == -1:
                queue.append(i)
                check[i] = check[popdata] + 1
                if i == b - 1:
                    return check[i]

    return -1


n = int(input())
data = list(map(int, input().split()))
a, b = map(int, input().split())
print(bfs(a, b, data, n))
