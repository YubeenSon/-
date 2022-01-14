###
# 백트래킹, 배제와 풀이 시간 단축...
###

import sys
N = int(sys.stdin.readline())

A = []
operator = []

for i in range(2):
    input = sys.stdin.readline()
    input_split = input.split()
    for j in input_split:
        if(i < 1):
            A.append(j)
        else:
            operator.append(j)

def calculate(x, y, mode):
    if(mode == 0):
        return x + y
    elif(mode == 1):
        return x - y
    elif(mode == 2):
        return x * y
    else:
        return x % y

# 재귀...모두 시도하기..
def recur(count, mode, result):
    # 종료조건
    if count == 1:
        # 그거대로 계산해 return
        A[count + 1] = calculate(A[count], A[count + 1], mode)
        return 

    return # 연산 결과 + 다음에 할거(4개 컴마로 리턴?)




for i in range(4):
    # 맨 앞에 연산하기
    for j in range(4):
        # 다음꺼 연산하기
        # 이런 걸 재귀로 작성하기