def solution(arr):
    answer = []
    for i in range(len(arr)):
        try:
            if arr[i] != answer[len(answer)-1]:
                answer.append(arr[i])
        except:
            answer.append(arr[i])
    return answer

print(solution(list(input().split())))
print(solution(list(input().split())))