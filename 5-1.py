N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for i in range(N):
    graph.append(list(map(int, input())))

def dfs(i, j):
    if i<0 or i>=M or j<0 or j>=N:
        return False

    if graph[i][j] == 0:
        graph[i][j] = 1

        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j-1)
        dfs(i, j+1)
        return True
    return False

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1
print(result)