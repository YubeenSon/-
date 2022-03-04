import sys

def input_data():
    N, K = list(map(int, sys.stdin.readline().split(" ")))
    coins = []
    for _ in range(N):
        coin = int(sys.stdin.readline())
        coins.append(coin)
    return N, K, coins

def solve():
    N, K, coins = input_data()
    coin_num = 0
    for i in coins[::-1]:
        if i > K:
            coins.pop()
        else:
            coin_num += K // i
            K = K % i
    print(coin_num)
solve()