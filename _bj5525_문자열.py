import sys
"""
slice가 아닌 탐색이었다...
탐색이 시간 많이 걸릴 것 같았는데 
index 이동하며 시간 줄일 수 있음
"""
N = int(sys.stdin.readline())
s_length = int(sys.stdin.readline())
S = sys.stdin.readline()[:-1]

answer = 0
str_count = 0
idx = 1

while idx < s_length:
    if S[idx:idx + 3] == "IOI":
        str_count += 1
        idx += 2
        if str_count == N:
            answer += 1
            # 이어 있을 수 있으니 answer로 확인된 하나만 빼주기
            str_count -= 1 
    else:
        str_count = 0 # 아얘 초기화
        idx += 1

print(answer)
