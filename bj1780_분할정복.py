import sys

"""
시간초과에 있어 조금 도움받은 문제..!
시간초과의 이유가 함수 인자로 arr을 전달할때마다 arr이 복사된다고 하는데
큰 크기의 배열이 복사되면 그만큼 시간이 늘어나기때문에 시간초과가 일어나는 것이었다!
"""

minus = 0
zero = 0
one = 0

def input_data():
    N = int(sys.stdin.readline())
    global arr
    arr = [[-1 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        temp = list(map(int, sys.stdin.readline().split(' ')))
        for j in range(N):
            arr[i][j] = temp[j]
        
    return N, arr

def search_area(x0, x1, y0):
    width = x1 - x0
    first_num = arr[y0][x0]
    all_same = True
    for i in range(width):
        for j in range(width):
            if(arr[y0 + i][x0 + j] != first_num):
                all_same = False
                return all_same, first_num
    return all_same, first_num


def recur(x0, x1, y0, y1, N):
    global minus
    global zero
    global one
    stride = N // 3
    all_same, first_num = search_area(x0, x1, y0)
    if(all_same == True):
        if(first_num == -1):
            minus += 1
        elif(first_num == 0):
            zero += 1
        else:
            one += 1
    
    else:
        recur(x0, x0 + stride, y0, y0 + stride, N // 3)
        recur(x0 + stride, x0 + (stride * 2), y0, y0 + stride, N // 3)
        recur(x0 + (stride * 2), x1, y0, y0 + stride, N // 3)

        recur(x0, x0 + stride, y0 + stride, y0 + (stride * 2), N // 3)
        recur(x0 + stride, x0 + (stride * 2), y0 + stride, y0 + (stride * 2), N // 3)
        recur(x0 + (stride * 2), x1, y0 + stride, y0 + (stride * 2), N // 3)

        recur(x0, x0 + stride, y0 + (stride * 2), y1, N // 3)
        recur(x0 + stride, x0 + (stride * 2), y0 + (stride * 2), y1, N // 3)
        recur(x0 + (stride * 2), x1, y0 + (stride * 2), y1, N // 3)

    return



def solve():
    global minus
    global zero
    global one
    N, arr = input_data()
    recur(0, N, 0, N, N)
    print(minus)
    print(zero)
    print(one)
    return

solve()