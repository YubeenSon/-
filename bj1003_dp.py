from sys import stdin
# 흑흑 시간초과....
# 단순 재귀로 피보나치 수를 구하면 왜 느릴까요? 
# 함수 호출의 개수가 기하급수적으로 늘어나기 때문입니다.

def input_data():
    """
    Input format
    
    """
    T = int(stdin.readline())
    cases = []
    for _ in range(T):
        num = int(stdin.readline())
        cases.append(num)
    
    return T, cases

def solve():
    # Input Data
    T, cases = input_data()
    answer_list = []
    max_case = max(cases)
    fibo = [[0, 0] for _ in range(max_case + 1)]
    fibo[0] = [1, 0]
    fibo[1] = [0, 1]
    for i in range(2, max_case + 1):
        fibo[i][0] = fibo[i - 1][0] + fibo[i - 2][0]
        fibo[i][1] = fibo[i - 1][1] + fibo[i - 2][1]
    
    for case in cases:
        answer = fibo[case]
        print(answer[0], end=' ')
        print(answer[1])

    return answer_list

answer = solve()