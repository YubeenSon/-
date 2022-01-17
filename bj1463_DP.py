import sys
# 크흐 2트에 클리어!
def input_data():
    N = int(sys.stdin.readline())
    return N

def solve():
    N = input_data()
    target = N
    dp = [0 for _ in range(N)]
    for i in range(1, N):
        candi1 = dp[i - 1] + 1
        if((i + 1) % 2 == 0):
            candi2 = dp[i // 2] + 1
        else:
            candi2 = 99999999
        if((i + 1) % 3 == 0):
            candi3 = dp[i // 3] + 1
        else:
            candi3 = 99999999
        dp[i] = min(candi1, candi2, candi3)
    answer = dp.pop()
    print(answer)
    return answer

solve()