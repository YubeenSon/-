from sys import stdin
# 오랜만에 그냥 맞췄다...!!! 
# 이진탐색의 근본

def input_data():
    """
    Input format
    
    """
    N = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))
    
    target_num = int(stdin.readline())
    targets = list(map(int, stdin.readline().rstrip().split()))

    return N, arr, target_num, targets


def solve():
    # Input Data
    N, arr, target_num, targets = input_data()
    # 이진탐색
    arr = sorted(arr)
    # 여기서 start, end, mid는 모두 index다!
    

    for target in targets:
        start = 0
        end = len(arr) - 1
        result = 0
        while start <= end:
            mid = (start + end) // 2

            if(target == arr[mid]):
                result = 1
                break
            elif(target < arr[mid]):
                end = mid - 1
            else:
                start = mid + 1

        print(result)                


    return result



answer = solve()