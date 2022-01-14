import sys
N = int(sys.stdin.readline())

steps = [0 for _ in range(301)]
dp = [0 for _ in range(301)]

for i in range(N):
    steps[i] = int(sys.stdin.readline())

# 이건 계단이 하나고 걔가 도착이니까 밟아야 하는 것
dp[0] = steps[0]
# 문제를 잘못 이해해 해결이 늦어진 문제
# 이 경우도 시작,1번째,2번째(도착)
# 시작 계단은 빼고 첫 계단부터 밟을지 안 밟을지 고르면 됨
dp[1] = steps[0] + steps[1]
# 이 부분에서 틀려서 고생했당
# 시작은 계단이 아니어서 [2]는 확실히 밟아야하는게 맞지만 0과 1중에 밟을거 선택 가능
dp[2] = max(steps[0] + steps[2], steps[1] + steps[2])

for n in range(3, N):
    dp[n] = max((steps[n] + steps[n - 1] + dp[n - 3]), (steps[n] + dp[n - 2]))
# print(dp)
print(dp[N - 1])