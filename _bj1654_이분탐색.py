import sys
"""
이분탐색은 기본이 start, end두고 
start <= end 일동안
mid에서의 상황 보고 범위 조절

도움 받은 부분 : https://www.acmicpc.net/board/view/70306
ZeroDivisionError의 경우 따로 처리하기보다 나눠주는 값을 max(mid, 1)로 처리해 통과
"""

def input_data():
    first_line = list(map(int, sys.stdin.readline().split( )))
    K = first_line[0]
    N = first_line[1]
    lines = [0 for _ in range(K)]
    for i in range(K):
        line = int(sys.stdin.readline())
        lines[i] = line
    return K, N, lines

def get_line_num(line, mid):
    return line // mid

def solve():
    K, N, lines = input_data()
    start = 0
    end = max(lines) # 초반에 틀린 부분
    max_length = 0

    while start <= end:
        mid = (start + end) // 2
        # ZeroDivisionError 생겨서 mid가 0일때를 따로 처리하는 것이 아니라
        # 나눠주는 수의 최소값이 1이 되도록 max(mid, 1)로 처리해 통과
        total_line_num = sum([get_line_num(i, max(mid, 1)) for i in lines])
        if(total_line_num >= N):
            max_length = mid
            start = mid + 1
        else:
            end = mid - 1

    print(max_length)
    return

solve()