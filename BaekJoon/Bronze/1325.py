from sys import stdin, stdout
from collections import deque, defaultdict
input = stdin.readline
"""
!! 어느회사를 해킹하려고한다.
1. 회사는 N개의 컴퓨터로 이루어져있는데 귀찮아서 한번의 해킹으로 여러개의 컴퓨터를 해킹!!
2-1. 회사의 컴퓨터는 신뢰하는 관계와, 신뢰하지않는 관계로 이루어짐.
2-2. A가 B를 신뢰하면 B를 해킹하면 A도 해킹당함.
3. 신뢰하는 관계가 주어졌을때 한번에 가장 많은 컴퓨터를 해킹할 수있는 번호를 출력!!
"""


def bfs(start):
    cnt = 1
    visited = [False for _ in range(n+1)]
    visited[start] = True
    queue = deque([start])
    while queue:
        popdata = queue.popleft()
        for i in data[popdata]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt += 1
    return cnt


n, m = map(int, input().split())
data = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    data[b].append(a)

results = []
max_cnt = 1

for i in range(1, n+1):
    cnt = bfs(i)
    if cnt > max_cnt:
        max_cnt = cnt
        results.clear()
        results.append(i)
    elif cnt == max_cnt:
        results.append(i)
print(*results)
