from itertools import combinations

def differ(a, b):
    if a > b: return a - b
    else: return b - a

def solution(n, wires):
    answer = n
    for cutted_wire in combinations(wires, len(wires)-1):
        group1 = []
        group2 = []
        extra = []
        for link in cutted_wire:
            # group1에 연결되어 있거나, 첫 시작인 경우
            if link[0] in group1 or link[1] in group1 or (len(group1) == 0 and len(group2) == 0):
                group1.extend(link)
            # group2에 연결된 경우
            elif link[0] in group2 or link[1] in group2:
                group2.extend(link)
			# 아직 어디에 연결되어 있는지 확실하지 않는 경우
            else:
                extra.append(link)
        # 아직 어디에 연결되어있는지 확실하지 않을 경우들을 다시 확인하기
        while extra:
            change = 0
            tmp_extra = []
            # 같은 방식으로 연결된 그룹을 확인해보되, change 값 추가
            for link in extra:
                if link[0] in group1 or link[1] in group1:
                    group1.extend(link)
                    change = 1
                elif link[0] in group2 or link[1] in group2:
                    group2.extend(link)
                    change = 1
                else:
                    tmp_extra.append(link)
            extra = tmp_extra
            # 전혀 갱신되지 않는 경우는 통째로 group2에 넣어주기
            if change == 0:
                for x in extra:
                    group2.extend(x)
                break
        
        # 중복제거
        group1 = len(set(group1))
        group2 = len(set(group2))
        
        # 송전탑 1개만 남은 경우
        if group1 == n-1:
            group2 = 1
        
        # 차이가 가장 작은 경우 갱신
        answer = min(answer, differ(group1, group2))
        
        # early return
        if answer == 0:
            return answer
    return answer