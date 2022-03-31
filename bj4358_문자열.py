import sys
"""
float에 대한 round() 의 동작은 예상과 다를 수 있습니다. 
부동소수로 인해 반올림이 제대로 안 될 수 있다...
f-string에서의 format 지정 방법은 {tree_rate:.4f}
%을 이용한 포맷팅은 변수 타입에 맞춰줘야 함
%s : 문자열, %d : 정수, %f : 실수
%.2f : 소수점 둘째자리까지만 표현되도록 반올림하라
"""

trees = {}
tree_cnt = 0
for line in sys.stdin:
    if line == '\n':
        break
    tree = line.rstrip()
    tree_cnt += 1
    if tree in trees:
        trees[tree] += 1
    else:
        trees[tree] = 1

sorted_keys = sorted(list(trees.keys()))

for key in sorted_keys:
    tree_rate = trees[key] / tree_cnt * 100
    print(f'{key} {tree_rate:.4f}')