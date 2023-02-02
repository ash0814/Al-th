from collections import deque

def solution(prices):
    answer = []
    dq_prices = deque(prices)
    
    while dq_prices:
        cur_price = dq_prices.popleft()
        time = 0
        for next_price in dq_prices:
            time += 1
            if cur_price > next_price:
                break
        answer.append(time)
    return answer

print(solution(list(map(int, (input().split())))))
