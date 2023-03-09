from collections import deque

def solution(begin, target, words):
    route = deque()
    visited = deque()
    route.append(begin)
    depth = -1
    
    while (words):
        new_route = deque()
        depth += 1
        while (route):
            cur_word = route.popleft()
            if cur_word == target:
                return depth
            for word in words:
                if word in visited:
                    continue
                cnt = 0
                for c, w in zip(cur_word, word):
                    if c != w:
                        cnt += 1
                    if cnt > 1:
                        break
                if cnt == 1:
                    new_route.append(word)
                    visited.append(word)
                    visited = list(set(visited))
        if len(new_route) == 0:
            return 0
        while (new_route):
            route.append(new_route.pop())
    return 0