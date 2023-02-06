def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    print(citations)
    # citations의 0부터 N까지
    for i in range(len(citations)):
        # 인용 횟수가 논문 개수보다 작거나 같을 때부터
        if (citations[i] <= len(citations)):
            print("[%d]"%i, "%d회 이상 인용된 논문: %d편"%(citations[i], i+1))
            try:
                # count 하나씩 줄여가며 논문 편수, 인용 횟수 비교하기
                for cnt in range(citations[i], -1, -1):
                    print("Count:", cnt)
                    print("%d회 이상 인용된 논문: %d편"%(cnt, i+1))
                    if (i+1 >= cnt):
                        return cnt
                break
            except:
                return citations[i]
    # 모든 인용 횟수들이 논문 개수보다 많은 경우
    return len(citations)


print(solution(list(map(int, list(input().split())))))
