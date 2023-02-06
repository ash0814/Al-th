def solution(clothes):
    answer = 1
    closet = {}
    for item, category in clothes:
        if category in closet:
            closet[category].append(item)
        else:
            closet[category] = [item]
    for cloth in closet.values():
        # 아이템을 선택하지 않은 경우 +1
        answer *= (len(cloth) + 1)
    
    # 최소 한개의 의상은 입어야 하므로 어떠한 아이템도 선택하지 않은 경우 -1
    return answer - 1