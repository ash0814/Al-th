import heapq

def solution(operations):
    heap = []
    for command in operations:
        com = command.split()
        if com[0] == 'I':
            heapq.heappush(heap, int(com[1]))
        elif com[0] == 'D':
            if len(heap) == 0:
                continue
            if com[1] == '1':
                tmp_heap = []
                for i in range(len(heap) - 1):
                    heapq.heappush(tmp_heap, heapq.heappop(heap))
                heap = tmp_heap
            elif com[1] == '-1':
                heapq.heappop(heap)
    heap.sort(reverse=True)
    if len(heap) < 2:
        return [0,0]
    else:
        return [heap[0], heap[-1]]