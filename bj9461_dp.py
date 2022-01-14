import sys
# 원킬!
def input_data():
    N = int(sys.stdin.readline())
    cases = []
    for _ in range(N):
        case = int(sys.stdin.readline())
        cases.append(case)

    return cases

def solve():
    cases = input_data()
    arr = [0 for _ in range(max(cases))]
    arr[:3] = 1, 1, 1
    arr[3] = 2
    arr[4] = 2
    for i in range(5 , max(cases)):
        arr[i] = arr[i - 5] + arr[i - 1]

    for case in cases:
        print(arr[case - 1])

    
solve()