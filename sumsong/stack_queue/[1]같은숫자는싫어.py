def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in range(len(arr)):
        try:
            if arr[i] != answer[len(answer)-1]:
                answer.append(arr[i])
        except:
            answer.append(arr[i])
    return answer

print(solution(list(input().split())))
print(solution(list(input().split())))