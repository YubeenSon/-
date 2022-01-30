import sys
"""
오잉도잉 맞춰버렸다..!
이 문제는 출력 순서가 중요했고
x, y를 잘 설정하는게 중요했다!!
"""


def input_data():
    N = int(sys.stdin.readline())
    arr = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        line = list(sys.stdin.readline())
        for j in range(N):
            arr[i][j] = line[j]
    return N, arr 

def search_area(arr, x0, x1, y0, y1):
    width = x1 - x0
    first_num = arr[y0][x0]
    all_same = True
    for i in range(width):
        for j in range(width):
            if(arr[y0 + i][x0 + j] != first_num):
                all_same = False
    return all_same, first_num


def recur(arr, x0, x1, y0, y1):
    # 종료조건 : 모든 면적이 같은 색
    all_same, first_num = search_area(arr, x0, x1, y0, y1)
    stride = x1 - x0
    if(all_same == True):
        print(first_num, end="")
        return
    else:
        print("(", end="")
        recur(arr, x0, x0 + stride // 2, y0, y0 + stride // 2)
        recur(arr, x0 + stride // 2, x1, y0, y0 + stride // 2)
        recur(arr, x0, x0 + stride // 2, y0 + stride // 2, y1)
        recur(arr, x0 + stride // 2, x1, y0 + stride // 2, y1)
        print(")", end="")
        return

def solve():
    N, arr = input_data()
    recur(arr, 0, N, 0, N)
    return

solve()