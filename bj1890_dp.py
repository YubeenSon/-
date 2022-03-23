import sys
from collections import deque
"""
부기's 솔루션
"""
def input_data():
    N = int(sys.stdin.readline())
    game = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        line = list(map(int, sys.stdin.readline().split(" ")))
        game[i] = line
    return N, game

def solve():
    N, game = input_data()
    dp = [[0 for _ in range(N)] for _ in range(N)]
    dp[0][0] = 1
    for r in range(N):
        for c in range(N):
            if dp[r][c] == 0 :
                continue
            if r == N - 1 and c == N - 1:
                continue
            value = game[r][c]

            newr = r + value
            if newr < N:
                dp[newr][c] += dp[r][c]

            newc = c + value
            if newc < N:
                dp[r][newc] += dp[r][c]

    print(dp[N - 1][N - 1])

solve()