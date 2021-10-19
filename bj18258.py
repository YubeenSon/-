####
# 1. list를 쓰면 pop(0)에서 O(1)을 이루지 못한다
# 2. import queue 가능은 한데 indexing이 안된다.
# 3. deque 짱이다. 기능도 많고 indexing 가능하다~!
###


from collections import deque
import sys
N = int(sys.stdin.readline())

dq = deque([])
size = 0

for i in range(N):
    order = sys.stdin.readline()
    order_split = order.split()
    command = order_split[0]
    if(command == "push"):
        dq.append(order_split[1])
        size += 1
    elif(command == "front"):
        if(size < 1):
            print("-1")
        else:
            print(dq[0])
    elif(command == 'back'):
        if(size < 1):
            print("-1")
        else:
            print(dq[size - 1])
    elif(command == "size"):
        print(size)
    elif(command == "empty"):
        if(size < 1):
            print("1")
        else:
            print("0")
    elif(command == "pop"):
        if(size < 1):
            print("-1")
        else:
            print(dq[0])
            dq.popleft()
            size -= 1