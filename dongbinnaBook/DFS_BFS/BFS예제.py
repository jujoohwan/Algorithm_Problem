from collections import deque
from sys import stdin, stdout


def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재노드를 방문처리
    visited[start] = True

    # 큐가 빌때 까지 반복
    while queue:
        v = queue.popleft()
        stdout.write(str(v) + ' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


# 각 노드가 연결된 정보를 표현(2차원 리스트) 인접리스트
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
# 각 노드가 방문된 정보를 표현
visited = [False] * 9
bfs(graph, 1, visited)
stdout.write('\n')
