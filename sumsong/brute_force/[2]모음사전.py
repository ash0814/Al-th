from itertools import product
import heapq

def solution(word):
    alpha = ['A', 'E', 'I', 'O', 'U']
    
    # 힙으로 풀었을 때 최소 0.96ms, 최대 3.28ms
    heap = []
    for length in range(1, len(alpha) + 1):
        for w in product(alpha, repeat=length):
            heapq.heappush(heap, ''.join(w))
    index = 0
    while True:
        index += 1
        if word == heapq.heappop(heap):
            return index
    
    # 리스트+sort로 풀 때 최소 0.76ms, 최대 1.59ms
    dic = []
    for length in range(1, len(alpha) + 1):
        for w in product(alpha, repeat=length):
            dic.append(''.join(w))
    dic.sort()
    return (dic.index(word) + 1)