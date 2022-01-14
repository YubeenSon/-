from sys import stdin
from collections import Counter
# while문을 포함한 코드에서는 while문에서 터지는 것 때문에 시간초과가 뜰 수도 있다(지금 그렇다)
# 아니었다. 지금은 count함수를 써서 그랬다. count는 선형탐색?이어서 그랬다는 이야기..
# 그래서 count 대신에 계수정렬을 쓰려 한다.
# 계수정렬 안 쓰고 dictionary로 쓰는건 시간 오래걸린다 쉬익쉬익(정말 count때문인가)
# count가 O(N)이다. 그 자체로..차라리 from collections import Counter이 낫다.

def input_data():
    """
    Input format
    
    """
    N = int(stdin.readline())
    cards = list(map(int, stdin.readline().split()))
    
    target_num = int(stdin.readline())
    targets = list(map(int, stdin.readline().rstrip().split()))

    return N, cards, target_num, targets


def solve():
    # Input Data
    N, cards, target_num, targets = input_data()
    # 이진탐색
    # 여기서 start, end, mid는 모두 index다!
    answer_list = []
    unique_cards = sorted(list(set(cards))) # 아니 set로 바꿨는데 왜 -10이 맨 뒤로 간다냐
    card_dict = Counter(cards)
    print(card_dict)
    # for card in unique_cards:
    #     card_num = cards.count(card)
    #     card_dict[card] = card_num

    for target in targets:
        if target in card_dict.keys():
            answer_list.append(card_dict[target])
        else:
            answer_list.append(0)

    for i in answer_list:
        print(i, end = ' ')
    return answer_list



answer = solve()