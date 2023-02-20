import heapq
from collections import deque

def case_of_wait(request):
    global cur_time, time
    wait_time = cur_time - request[0]
    cur_time += request[1]
    time += wait_time + request[1]
    
def case_of_spend(request):
    global cur_time, time
    spend_time = request[0] - cur_time
    cur_time += spend_time + request[1]
    time += request[1]
    
def solution(jobs):
    global time, cur_time
    cnt = len(jobs)
    heapq.heapify(jobs)
    first = heapq.heappop(jobs)
    time = first[1]
    cur_time = first[0] + first[1]
    wait = deque()
    while jobs:
        # 대기중인 작업 wait에 걸러내기
        while jobs:
            request = heapq.heappop(jobs)
            if request[0] > cur_time:
                heapq.heappush(jobs, request)
                break
            wait.append(request)
        # 대기중인 작업이 있을 때
        if wait:
            wait = sorted(wait, key=lambda x:(x[1], x[0]), reverse=True)
            request = wait.pop()
            case_of_wait(request)
            while wait:
                heapq.heappush(jobs, wait.pop())
        # 작업을 수행하고 있지 않을 때
        else:
            request = heapq.heappop(jobs)
            if request[0] >= cur_time:
                case_of_spend(request)
            else:
                case_of_wait(request)
    return time // cnt