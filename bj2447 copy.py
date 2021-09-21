# GG
# 참고 페이지 : https://leedakyeong.tistory.com/entry/%EB%B0%B1%EC%A4%80-python-2447%EB%B2%88-%EB%B3%84-%EC%B0%8D%EA%B8%B0-10
n = int(input())

result = [["*"]*n for _ in range(n)]

v = n
count = 0
while v != 1:
    v /= 3
    count += 1
# 몇 승인지 구하기
# 지울 별 확인
for cnt in range(count):
    idx = [i for i in range(n) if (i // 3 ** cnt) % 3 == 1]
    for i in idx:
        for j in idx:
            result[i][j] = " "


for i in range(n):
    for j in range(n):
        print(result[i][j], end="")
    print()