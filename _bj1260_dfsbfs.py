import sys
from collections import deque
"""
set은 append가 아니라 add
set이 정렬되었다는 것을 보장 못하므로 
땜빵으로 min, max값을 queue, stack에 넣는 것으로 대체(이 부분 도움받아 해결)
https://www.acmicpc.net/board/view/73045
"""
def input_data():
    N, M, V = list(map(int, sys.stdin.readline().split( )))
    adj_list = {}
    # dict 초기화
    for i in range(1, N + 1):
        adj_list[i] = set()
    for i in range(M):
        line = list(map(int, sys.stdin.readline().split( )))
        adj_list[line[0]].add(line[1])
        adj_list[line[1]].add(line[0])
    return N, M, V, adj_list

def dfs(graph, start):
    visited = []
    stack = [start]
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            candi = graph[n] - set(visited)
            for i in range(len(candi)):
                num = max(candi)
                candi.remove(num)
                stack.append(num)
    return visited
    
def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            candi = graph[n] - set(visited)
            for i in range(len(candi)):
                num = min(candi)
                candi.remove(num)
                queue.append(num)
    return visited

def print_result(arr):
    for i in range(len(arr)):
        if(i != len(arr) - 1):
            print(arr[i], end=' ')
        else:
            print(arr[i])

def solve():
    N, M, V, adj_list = input_data()
    dfs_result = dfs(adj_list, V)
    bfs_result = bfs(adj_list, V)
    print_result(dfs_result)
    print_result(bfs_result)    
    return

solve()