import sys
from collections import deque
"""
오타때문에....오타..때문에...
"""
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
global cnt
cnt = 0

def bfs(N, x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    global cnt
    cnt += 1

    while queue:
        tempx, tempy = queue.popleft()
        for i in range(4):
            newx = tempx + dx[i]
            newy = tempy + dy[i]
            if newx < 0 or newx >= N or newy < 0 or newy >= N:
                continue
            else:
                if(graph[newx][newy] == 1):
                    graph[newx][newy] = 0
                    cnt += 1
                    if (newx, newy) not in queue:
                        queue.append((newx, newy))

N = int(sys.stdin.readline())
graph = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    line = str(sys.stdin.readline())
    for j in range(N):
        graph[i][j] = int(line[j])
result = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            cnt = 0
            bfs(N, i, j)
            result.append(cnt)
            
result.sort()
print(len(result))
for i in result:
    print(i)