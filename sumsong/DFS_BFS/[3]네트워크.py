from collections import deque

def solution(n, computers):
    network = 0
    total = deque([x for x in range(n)])
    route = deque()
    visited = deque()
    while total:
        node = deque.popleft(total)
        deque.append(route, node)
        network += 1
        # print("node:", node, "total: ", total, "route:", route, "visited:", visited)
        while route:
            node = deque.popleft(route)
            if node in total:
                total.remove(node)
            deque.append(visited, node)
            for i in range(n):
                if computers[node][i] == 1 and i not in visited:
                    deque.append(route, i)
    return network

# 전체[1 2 3 4 5] 둘러볼 곳[] 둘러본 곳[]
# 1을 뽑았어
# [1]을 쭉 둘러봐
# 연결되어 있는 애를 둘러볼 곳에 넣어 둘러본 곳은 제외
# 전체[2 3 4 5] 둘러볼 곳[3 5] 둘러본 곳[1]
# 둘러볼 곳[3]
# [3]을 쭉 둘러봐
# 연결되어 있는 애를 둘러볼 곳에 넣어 둘러본 곳은 제외
# 전체[2 4 5] 둘러볼 곳[5] 둘러본 곳[1 3]
# [5]를 쭉 둘러봐
# 연결되어 있는 애를 둘러볼 곳에 넣어 둘러본 곳은 제외
# 전체[] 둘러볼 곳[] 둘러본 곳[1 3]