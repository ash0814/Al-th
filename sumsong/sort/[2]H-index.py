def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    # citations의 0부터 N까지
    for i in range(len(citations)):
        if i >= citations[i]:
            return i
    # 모든 인용 횟수들이 논문 개수보다 많은 경우
    return len(citations)