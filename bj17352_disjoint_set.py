import sys
"""
input단에서 괄호 빼먹는 등 실수하지 말기..!
join함수는 list 안의 요소들이 str일때 가능
"""
N = int(sys.stdin.readline())
graph = [i for i in range(N + 1)]
bridges = [[0, 0] for _ in range(N - 2)]
for i in range(N - 2):
    conneted = list(map(int, sys.stdin.readline().split(" ")))
    bridges[i] = conneted

def get_parent(node_num):
    if graph[node_num] == node_num:
        return node_num
    return get_parent(graph[node_num])

def union_parent(node1, node2):
    n1_parent = get_parent(node1)
    n2_parent = get_parent(node2)
    graph[max(n1_parent, n2_parent)] = min(n1_parent, n2_parent)
        
for n1, n2 in bridges:
    union_parent(n1, n2)

# 추가 후에 한번 더 부모 제대로 연결해주기
for i in range(1, N + 1):
    graph[i] = get_parent(i)

unique_node_num = map(str, list(set(graph[1:])))
print(' '.join(unique_node_num))
