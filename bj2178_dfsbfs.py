import sys
from collections import deque
"""
예제는 다 맞는데 시간초과....
visited를 list로 하지 말고 graph와 같은 크기의 matrix를 만들고
방문한다면 1로 바꾸기
list에서의 in은 O(N)
"""
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def input_data():
    N, M = list(map(int, sys.stdin.readline().split()))
    graph = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        line = str(sys.stdin.readline())
        for j in range(M):
            graph[i][j] = int(line[j])
    return N, M, graph

def bfs(graph, N, M):
    visited = [[0] * M for _ in range(N)]
    queue = deque()
    start = (0, 0)
    queue.append(start)
    zeros = [[0 for _ in range(M)] for _ in range(N)]
    zeros[0][0] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            newx = x + dx[i]
            newy = y + dy[i]
            if newx < 0 or newx >= N or newy < 0 or newy >= M:
                continue
            elif graph[newx][newy] == 0:
                continue
            elif visited[newx][newy] == 1:
                continue
            else:
                zeros[newx][newy] = zeros[x][y] + 1
                queue.append((newx, newy))
                visited[newx][newy] = 1
    return zeros

def solve():
    N, M, graph = input_data()
    zeros = bfs(graph, N, M)
    print(zeros[N - 1][M- 1])

solve()