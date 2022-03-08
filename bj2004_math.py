import sys

"""
len(list(itertools.combinations(n_list, m))) <= 메모리초과
조합 구하는 식 그대로(with math.factorial) 구현 <= 시간초과
곱셈이 아니라 range자체에서 시간초과 발생하는 것으로 보임
(n이 가진 5, 2 개수)((n - m)이 가진 5, 2개수)/(m이 가진 5, 2개수) 이런 식으로 계산해
10이 나올 수 있는가 판별
"""

def input_data():
    n, m = map(int, sys.stdin.readline().split(" "))
    return n, m

def count_multiple(num, multiple):
    result = 0
    mult = multiple
    while True:
        if num // multiple == 0:
            break
        else:
            result += num // multiple
            multiple *= mult
    return result

def solve():
    n, m = input_data()
    upper_five = count_multiple(n, 5)
    upper_two = count_multiple(n, 2)
    temp_five = count_multiple((n - m), 5)
    temp_two = count_multiple((n - m), 2)
    lower_five = count_multiple(m, 5)
    lower_two = count_multiple(m, 2)

    five = upper_five - lower_five - temp_five
    two = upper_two - lower_two - temp_two
    result = min(five, two)
    # print(upper_five, upper_two, lower_five, lower_two)
    print(max(result, 0))
solve()