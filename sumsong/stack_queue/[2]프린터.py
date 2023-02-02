from collections import deque

def solution(priorities, location):
    answer = 0
    dq = deque(priorities)
    cnt = len(dq)
    
    while (len(dq) > 0):
        if (dq[0] == max(dq)):
            dq.popleft()
            if (location == 0):
                return (cnt - len(dq))
            location -= 1
        else:
            dq.append(dq.popleft())
            if location == 0:
                location = len(dq) - 1
            else:
                location -= 1
    return answer

print("ans", solution(list(map(int, input().split())), int(input())))
print("ans", solution(list(map(int, input().split())), int(input())))