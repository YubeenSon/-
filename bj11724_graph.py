import sys

node_num, edge_num = list(map(int, sys.stdin.readline().split(" ")))
graph = [[] for _ in range(node_num + 1)]
for i in range(edge_num):
    start, end = list(map(int, sys.stdin.readline().split(" ")))
    graph[start].append(end)
    graph[end].append(start)
visited = [False for _ in range(node_num + 1)]

def dfs(graph, start):
    stack = []
    stack.append(start)
    visited[start] = True

    while stack:
        n = stack.pop()
        for i in graph[n]:
            if not visited[i]:
                stack.append(i)
                visited[i] = True

count = 0
for i in range(1, node_num + 1):
    if not visited[i]:
        count += 1
        dfs(graph, i)
print(count)