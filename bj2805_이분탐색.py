from sys import stdin
# 문제 있는 예시
# 2 3   2 1
# 2 2   2 2
# '적어도'라는 단어때문에 완벽히 요구하는 양과 같은 양을 얻지 못할 수 있다.
# + 이진탐색은 start, end바꿔줄 때 +1, -1 해줘야햔다

def input_data():
    """
    Input format
    
    """
    N, M = map(int, stdin.readline().split())

    row = list(map(int, stdin.readline().rstrip().split()))

    return N, M, row


def get_tree(tree, mid):
    total = 0
    for i in tree:
        if(i > mid):
            rest = i - mid
            total += rest
    # print(total)
    return total

def solve():
    # Input Data
    N, M, tree = input_data()

    start = 0
    end = max(tree)

    # Process
    while start <= end:
        mid = (start + end) // 2

        total_len = get_tree(tree, mid)
        # print(f'{total_len} {mid}')

        if total_len < M : # 덜 잘렸다(부족하다)
            end = mid - 1
        else: # 더 잘렸거나 같다
            result = mid
            start = mid + 1        
        # if (total_len == M):
        #     return mid # 적어도 큰거면 이 부분 필요 없음

        # 적어도 = 같거나 크다(적을때는 기록해놓을 필요 없음)
        # elif(total_len > M):
        #     result = mid
        #     start = mid + 1

        # elif(total_len < M):
        #     result = mid
        #     end = mid - 1
        
    return result



answer = solve()
print(answer)