import sys
"""
이분탐색은 항상 에러날 수 있는 케이스들 주의..
부등호는 한쪽 꼭 등호 넣어주기!
"""

N = int(sys.stdin.readline())
budgets = list(map(int, sys.stdin.readline().split(" ")))
total_budget = int(sys.stdin.readline())

start = 1
end = max(budgets)
limit = 0
result = 0

while start <= end:
    mid = (start + end) // 2
    sum_budget = 0
    for i in budgets:
        if i > mid:
            sum_budget += mid
        elif i <= mid:
            sum_budget += i

    # print(f'{start} {mid} {end} -> {sum_budget}')
    if sum_budget > total_budget:
        end = mid - 1
        # print('go down')
    else:
        limit = max(limit, sum_budget)
        start = mid + 1
        result = max(mid, result)
        # print('go up')

print(result)

"""
다른 풀이
[110 120 140 150 / 485] -> [127]
avg = 130
110 < avg 평균보다 작으니까 그냥 다 준다
budget = 375
avg = 125
120 < avg 평균보다 작으니까 그냥 다 준다
budget = 255
avg = 127
140 > avg -> return(평균보다 크다, 더는 못준다)

def getMaxAllocation(requests, N, budget):
    sortedRequests = sorted(requests)
    n = N
    for i in range(N):
        avg = budget // n
        if sortedRequests[i] > avg:
            return avg
        budget -= sortedRequests[i]
        n -= 1
    return sortedRequests[N-1]
"""