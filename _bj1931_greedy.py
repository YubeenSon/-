import sys
"""
소요시간보다 종료시간이 빠른 것으로 접근
"""
def input_data():
    N = int(sys.stdin.readline())
    meetings = []
    max_num = -1
    for i in range(N):
        start, end = list(map(int, sys.stdin.readline().split(" ")))
        if end > max_num:
            max_num = end
        meetings.append((start, end))
    return N, meetings, max_num

# 종료시간ver
def end_time_solve():
    N, meetings, max_num = input_data()
    meetings.sort(key=lambda x: x[0])
    meetings.sort(key=lambda x: x[1])
    result = 1
    end = meetings[0][1]
    for i in range(1, N):
        if meetings[i][0] >= end:
            result += 1
            end = meetings[i][1]
    print(result)

# 소요시간ver
def span_time_solve():
    N, meetings, max_num = input_data()
    result = 0
    time_check = [1 for _ in range(max_num + 1)]
    short_check = [1 for _ in range(max_num + 1)]
    time = [] # 중복되는 같은 회의 인식 못함, 중복된 키 불가
    for i in meetings:
        diff = i[1] - i[0]
        time.append((i, diff))
    sorted_time = sorted(time, key=lambda x : x[1])
    
    for i in range(len(sorted_time)):
        meeting = sorted_time[i][0]
        if sorted_time[i][1] == 0:
            short_check[meeting[0]] = 0
            result +=1
            continue
        if all(time_check[meeting[0]:meeting[1]]) and all(short_check[meeting[0] + 1:meeting[1]]):
            time_check[meeting[0]:meeting[1]] = [0 for _ in range(sorted_time[i][1])]
            result += 1
    print(result)

end_time_solve()