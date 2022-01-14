import sys
N = int(sys.stdin.readline())

meetings = []
for i in range(N):
    meet = sys.stdin.readline()
    meet_split = meet.split()
    meet_temp = (int(meet_split[0]), int(meet_split[1]))
    meetings.append(meet_temp)
[(1, 4), ]
meetings.sort()

meetings.sort(key = lambda x : x[1])
# print(meetings)

# count = 0
# for meet in meetings:
#     if(meet[1])

max_meeting = 0
for i, meet in enumerate(meetings):
    meet_end = meet[1]
    count = 1
    start_point = i
    while(meet_end <= max(meetings)[0]):
        for j in range(start_point, len(meetings)):
            if(meetings[j][0] >= meet_end):
                count += 1
                meet_end = meetings[j][1]
                start_point = j
                break
    max_meeting = max(max_meeting, count)

print(max_meeting)
