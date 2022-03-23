import sys
from collections import deque

dr = [1, 2, 2, 1, -1, -2, -2, -1]
dc = [2, 1, -1, -2, -2, -1, 1, 2]

T = int(sys.stdin.readline())
for _ in range(T):
    length = int(sys.stdin.readline())
    graph = [[0 for _ in range(length)] for _ in range(length)]
    now = list(map(int, sys.stdin.readline().split(" ")))
    goal = list(map(int, sys.stdin.readline().split(" ")))
    graph[now[0]][now[1]] = 1
    graph[goal[0]][goal[1]] = 1

    def bfs(x, y):
        count = 0
        visited = [[False for _ in range(length)] for _ in range(length)]

        queue = deque()
        queue.append((x, y, count))
        if [x, y] == goal:
            return count
        
        while queue:
            r, c, cnt = queue.popleft()
            for i in range(8):
                newr = r + dr[i]
                newc = c + dc[i]
                if [newr, newc] == goal:
                    cnt += 1
                    return cnt
                if newr < 0 or newr >= length or newc < 0 or newc >= length:
                    continue
                if not visited[newr][newc]:
                    visited[newr][newc] = True
                    # print(f'{newr} {newc}')
                    # cnt += 1
                    queue.append((newr, newc, cnt + 1))
            
    print(bfs(*now))
