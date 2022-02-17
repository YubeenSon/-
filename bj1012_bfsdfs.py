import sys

def input_data():
    T = int(sys.stdin.readline())
    width, height, num = list(map(int, sys.stdin.readline().split()))
    # 좌표로 adj_list 생성??
    field = [[0 for _ in range(width)] for _ in range(height)]
    for i in range(num):
        x, y = list(map(int, sys.stdin.readline().split( )))
        field[y][x] = 1
    return T, width, height, num, field

def solve():
    T, width, height, num, field = input_data()
    for i in range(height):
        print(field[i])

solve()