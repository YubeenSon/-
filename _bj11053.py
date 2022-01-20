import sys
# 놓친 반례 : 1 2 8 4 2 8(4), 5 1 2 3 4(4)
# 322 831 212 232 545 698 260 265 324 215 701 75 156 605 851 993 425 887 691 593(20)(8) 

# https://namu.wiki/w/%EC%B5%9C%EC%9E%A5%20%EC%A6%9D%EA%B0%80%20%EB%B6%80%EB%B6%84%20%EC%88%98%EC%97%B4
# 내가 놓친 부분 : arr[i]보다 작은 수 중 "dp[j]가 가장 큰 애 + 1"

def input_data():
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    return N, arr

def solve():
    N, arr = input_data()
    dp = [1 for _ in range(N)]
    start = 0
    for i in range(1, N):
        temp_idx = 0
        # arr[i]보다 작은 애들 중 dp[j]가 가장 큰 애
        for j in range(i):
            if(arr[j] < arr[i]):
                temp_idx = max(temp_idx, dp[j])
        dp[i] = temp_idx + 1    
        
    print(max(dp))

solve()