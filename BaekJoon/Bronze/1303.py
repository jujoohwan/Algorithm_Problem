from sys import stdin
from collections import deque
input = stdin.readline

# 핵심은 입력값이 적기때문에 2중리스트를 활용하여 blue,white 가 방문하였을때 cnt가 증가하게하여
# 인접한 

# x축 방향, y축 방향 리스트
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 가로길이, 세로길이
n, m = map(int, input().split())

# 아군,적군 2중리스트
graph = [list(input()) for _ in range(m)]
# 방문체크
visited = [[False] * n for i in range(m)]
# 아군, 적군
white, blue = 0, 0


def bfs(x, y, color):
    cnt = 0
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                # 색깔체크
                if graph[nx][ny] == color and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    cnt += 1
    return cnt+1


for i in range(m):
    for j in range(n):
        if graph[i][j] == 'W' and not visited[i][j]:
            white += bfs(i, j, 'W') ** 2
        elif graph[i][j] == 'B' and not visited[i][j]:
            blue += bfs(i, j, 'B') ** 2
print(white, blue)
