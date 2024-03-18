from sys import stdin, stdout
from collections import deque
n, m, v = map(int, stdin.readline().split())

visited = [False] * (n+1)






def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        data = queue.popleft()
        stdout.write(str(data) + ' ')
        for i in adj[data]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


def dfs(start):
    stdout.write(str(start) + ' ')
    visited[start] = True
    for i in adj[start]:
        if not visited[i]:
            dfs(i)
            visited[i] = True


adj = [[] for _ in range(n+1)]
for i in range(m):
    src, dest = map(int, stdin.readline().split())
    adj[src].append(dest)
    adj[dest].append(src)

# 작은 노드들 부터 방문해야하므로 sort()
for i in range(len(adj)):
    adj[i].sort()
dfs(v)
visited = [False] * (n+1)
stdout.write('\n')
bfs(v)
