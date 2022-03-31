import sys
import re
"""
정규표현식 써서 나누기 -> 일반 split처럼 나누는 기준도 사라짐
더하기 빼기 있는 식 최소로 만들기 -> 처음 나오는 빼기 기호 뒤로 나오는 숫자는 다 빼주기
sys.stdin.readline()으로 받아오면 맨 마지막에 \n이 붙는다.
"""
sentence = str(sys.stdin.readline())[:-1]
elements = re.split('[+-]', sentence)

"""
백준 풀이
equation = sentence.split('-')
ans = sum(map(int, equation[0].split('+'))) << 빼기 앞쪽에 있는 더하기들
for i in range(1, len(equation)):
    num_list = map(int, equation[i].split('+')) << 빼기 뒤에 있는 애들 혹시 있는 +까지 다 쪼개 넣어주기
    ans -= sum(num_list)
print(ans)
"""

cnt = 0
negative_flag = 0

for idx, i in enumerate(sentence):
    if i == "+":
        cnt += 1
    if i == '-':
        cnt += 1
        negative_flag = cnt
        break

if negative_flag == 0:
    positive_num = map(int, elements)
    negative_num = [0]
else:
    positive_num = map(int, elements[:negative_flag])
    negative_num = map(int, elements[negative_flag:])

positive_sum = sum(positive_num)
negative_sum = sum(negative_num)

print(positive_sum - negative_sum)


