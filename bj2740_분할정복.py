import sys

def input_data():
    N, M = map(int, sys.stdin.readline().split(" "))
    m1 = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        line = list(map(int, sys.stdin.readline().split(" ")))
        m1[i] = line
    M, K = map(int, sys.stdin.readline().split(" "))
    m2 = [[0 for _ in range(K)] for _ in range(M)]
    for i in range(M):
        line = list(map(int, sys.stdin.readline().split(" ")))
        m2[i] = line
    return N, M, K, m1, m2

def solve():
    N, M, K, m1, m2 = input_data()
    result = [[0 for _ in range(K)] for _ in range(N)]
    for i in range(N):
        for j in range(K):
            for a in range(M):
                result[i][j] += m1[i][a] * m2[a][j]
    
    for i in range(N):
        for j in range(K):
            print(result[i][j], end=' ')
        print()

solve()