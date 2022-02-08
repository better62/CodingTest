from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, input())))

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + x[i]
            ny = y + y[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                q.append((nx, ny))

    return graph[n-1][m-1]

print(bfs(0, 0))



