import sys
"""
따흑...힘들었다...
헤맨 부분
1. 2차원 배열에서 구역 설정
    - serch_color에서 i[x1:x2]로 안의 배열에 대해서 색깔을 본다
      (== paper[x1:x2]가 아니라 i[x1:x2]다)
    - 인덱스는 x0, x1, y0, y1로 설정하는 것이 편하며
      재귀로 들어가도 4개를 모두 이동하며 탐색해야하기때문에(sliding window)
      stride의 절반을 더해주는 식으로 한다.
      (x1, x1 + stride // 2, y1, y1 + stride // 2)
      
2. 문제 이해
    - 이 문제는 분할탐색인데 
    만일 해당 함수에서 타겟이 되는 전체가 같은수면 
    더이상 그 부분은 쪼개지 않는다!!
    == 종료조건이란 타겟 **면적**이 타겟 **크기**(level)만큼인가(?) 
"""

blues = 0
whites = 0

def input_data():
    N = int(sys.stdin.readline())
    paper = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        line = list(map(int, sys.stdin.readline().split()))
        paper[i] = line
    return N, paper

def search_color(paper, x1, x2, y1, y2):
    blue = 0
    white = 0
    
    for i in paper[y1:y2]:
        for j in i[x1:x2]:
            if(j == 1):
                blue += 1
            else:
                white += 1
    return blue, white

def recur(paper, x1, x2, y1, y2):
    global blues
    global whites
    # 종료조건 : 면적의 모든 색깔이 같은 경우
    blue, white = search_color(paper, x1, x2, y1, y2)
    stride = x2 - x1
    level = (x2 - x1) * (x2 - x1)
    if(blue == level):
        blues += 1
        return 
    elif(white == level):
        whites += 1 
        return
    # 다르다면 더 작은 단위에서 돌려본다
    else:
        return recur(paper, x1, x1 + stride // 2, y1, y1 + stride // 2), recur(paper, x1, x1 + stride // 2, y1 + stride // 2, y2), recur(paper, x1 + stride // 2, x2 , y1, y1 + stride // 2), recur(paper, x1 + stride // 2, x2 , y1 + stride // 2, y2)

def solve():
    N, paper = input_data()
    global blues
    global whites
    recur(paper, 0, N, 0, N)
    print(whites)
    print(blues)
    
solve()