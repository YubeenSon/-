import sys
# 도움 받은 문제...8ㅅ8
# 1. rgb값에 중복되는 값이 있는 경우도 있다.
# 2. 최소값만 찾아가는 것이 최소값이 되는 것은 아니다.
# 카테고리가 DP인 문제!!!
# DP의 특징인 점화식을 생성할 수 있다.!!

def input_data():
    N = int(sys.stdin.readline())
    costs = [[0, 0, 0] for _ in range(N)]
    for i in range(N):
        # list로 밖에 감싸줘야 함
        rgb = list(map(int, sys.stdin.readline().split()))
        costs[i] = rgb
    return N, costs

def solve():
    N, costs = input_data()

    for i in range(1, N):
        costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
        costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
        costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])

    print(min(costs[N - 1])) 

solve()
