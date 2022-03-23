import sys
"""
이중for문과 while 같이 있으면 탈출 어려우니 while문에 True 말고 조건걸기
이중for문 break는 스위치 변수로 조정
들여쓰기 주의!!
"""
def input_data():
    N, M = map(int, sys.stdin.readline().split(" "))
    square = [[0 for _ in range(M)] for _ in range(N)]
    for i  in range(N):
        line = list(sys.stdin.readline())
        square[i] = line[:-1]
    return N, M, square

def solve():
    N, M, square = input_data()
    max_square = min(N, M)

    def find_max_square_size(max_square_size):
        k = max_square_size - 1
        for r in range(N - k):
            for c in range(M - k):
                pivot = square[r][c]
                if(pivot == square[r][c + k] == square[r + k][c] == square[r + k][c + k]):
                    print(max_square_size * max_square_size)
                    return True 
        return False

    for max_square_size in reversed(range(max_square)):
        if find_max_square_size(max_square_size):
            return
    print(1)
    return

solve()