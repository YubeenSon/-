import sys
from collections import deque


N = int(sys.stdin.readline())
adj_list = {}
result = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    line = list(map(int, sys.stdin.readline().split(" ")))
    result[i] = line
    index_line = []
    for idx, num in enumerate(line):
        if num != 0:
            index_line.append(idx)
    adj_list[i] = index_line


for key in adj_list.keys():
    nexts = adj_list[key]
    visited = [] 

    queue = deque(nexts)


    while queue:
        next = queue.popleft()
        result[key][next] = 1
        if (key, next) not in visited:
            visited.append((key, next))
            for i in adj_list[next]:
                queue.append(i)

for i in range(N):
    for j in range(N):
        print(result[i][j], end=' ')
    print()

# 백준 코드
def dfs(node, g, visited):
    for i in adj_list[g]:
        if not visited[i]:
            visited[i] = True
            result[node][i] = 1
            dfs(node, i, visited)

for i in range(N):
    visited = [False] * N
    dfs(i, i, visited)