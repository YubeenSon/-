import sys
from collections import deque
"""
다음엔 내 코드 도움도 받지 않고 기억해서 풀어보기!
그리고 시간복잡도 향상해보기(visited에 dict 자료형 활용하기)
"""
def input_data():
    num_computer = int(sys.stdin.readline())
    connected_com = int(sys.stdin.readline())
    adj_list = {}

    for i in range(1, num_computer + 1):
        adj_list[i] = set()
    for i in range(connected_com):
        first, second = list(map(int, sys.stdin.readline().split()))
        adj_list[first].add(second)
        adj_list[second].add(first)
    return num_computer, connected_com, adj_list

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

def solve():
    num_com, connected_num, adj_list = input_data()
    bfs_result = bfs(adj_list, 1)
    print(len(bfs_result) - 1)
    return

solve()