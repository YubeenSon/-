import sys
import itertools

"""
GCD = Greatest Common Divisor = 최대공약수
시간초과 : 최대공약수 탐색을 큰수에서부터 역수로 접근하는 것으로 해결
(역순으로 왔으니 그게 최대공약수)
range 숫자 거꾸로 돌리려면 reversed(range(x, y))
"""

def input_data():
    t = int(sys.stdin.readline())
    cases = [[0] for _ in range(t)]
    for i in range(t):
        line = list(map(int, sys.stdin.readline().split(" ")))
        cases[i] = line[1:]
    return cases

def get_gcd(case):
    max_gcd = 1
    for i in reversed(range(1, max(case) + 1)):
        if(case[0] % i == 0) and (case[1] % i == 0):
            max_gcd = i
            break
    return max_gcd
            
def solve():
    cases = input_data()
    for case in cases:
        result = 0
        combs = list(itertools.combinations(case, 2))
        for j in combs:
            result += get_gcd(j)
        print(result)

solve()