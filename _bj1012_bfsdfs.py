import sys
from collections import deque
"""
참고 : https://hongcoding.tistory.com/72
좌표를 deque에 넣을때는 생성 당시에 같이 만들지 말고 tuple형태로 append한다.
"""
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, x, y, width, height):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0

    while queue:
        tempx, tempy = queue.popleft()
        for i in range(4):
            newx = tempx + dx[i]
            newy = tempy + dy[i]
            if newx < 0 or newx >= width or newy < 0 or newy >= height:
                continue
            else:
                if(graph[newx][newy] == 1):
                    graph[newx][newy] = 0
                    queue.append((newx, newy))

T = int(sys.stdin.readline())
for case in range(T):
    width, height, num = list(map(int, sys.stdin.readline().split()))
    field = [[0 for _ in range(height)] for _ in range(width)]
    for _ in range(num):
        x, y = map(int, sys.stdin.readline().split())
        field[x][y] = 1

    cnt = 0

    for i in range(width):
        for j in range(height):
            if field[i][j] == 1:
                bfs(field, i, j, width, height)
                cnt += 1
    print(cnt)