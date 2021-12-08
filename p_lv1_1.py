# 로또의 최고 순위와 최저 순위
def solution(lottos, win_nums):
    lottos_s = sorted(lottos)
    win_nums_s = sorted(win_nums)

    zeros = 0
    wins = 0
    last_same = 0

    for i, num in enumerate(lottos_s):
        if(num == 0):
            zeros += 1
        else:
            for j in range(last_same, 6):
                if(num == win_nums_s[j]):
                    wins += 1
                    last_same = j
                    # print(f'{i} {num} {win_nums_s[j]} {j}')
                    break
                elif (num < win_nums_s[j]):
                    # print(f'{i} {num} {win_nums_s[j]} {j}')
                    break
    print(wins)
    max_rank = min(7 - (wins + zeros), 6)
    min_rank = min(7 - (wins), 6)
    answer = [max_rank, min_rank]

    return answer