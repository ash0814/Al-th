# DFS로 풀었는데 효율성 테스트 fail

# 이동 우선순위
# 남쪽 [0, 1]
# 동쪽 [1, 0]
# 북쪽 [0, -1]
# 서쪽 [-1, 0]

min_route = 10000

def check_blocked(maps, n, m):
    if maps[m][n-1] == 0 and maps[m-1][n] == 0:
        return True
    return False

def recur(maps, me, n, m, cnt, route):
    global min_route
    
    # 최단거리 아니면 그냥 빨리 돌아가자
    if cnt > min_route:
        return

    x, y = me[0], me[1]
    
    # 적 진영에 도착한 경우
    if x == n and y == m:
        # print("도착!", me, cnt)
        if cnt < min_route:
            min_route = cnt
        return

    # 벽에 막히거나 좌표를 벗어난 경우
    if me in route:
        # print("! 왔던 길", route)
        return
    if x < 0 or x > n or y < 0 or y > m or maps[y][x] == 0:
        # print("! 막힌 길")
        return
    
    route = route + [me]
    
    # print("me :", me, "maps :", maps[y][x], "cnt :", cnt, "next[남] :", [x+y for x,y in zip(me, [0, 1])])
    recur(maps, [x+y for x,y in zip(me, [0, 1])], n, m, cnt+1, route)
    # print("me :", me, "maps :", maps[y][x], "cnt :", cnt, "next[동] :", [x+y for x,y in zip(me, [1, 0])])
    recur(maps, [x+y for x,y in zip(me, [1, 0])], n, m, cnt+1, route)
    # print("me :", me, "maps :", maps[y][x], "cnt :", cnt, "next[북] :", [x+y for x,y in zip(me, [0, -1])])
    recur(maps, [x+y for x,y in zip(me, [0, -1])], n, m, cnt+1, route)
    # print("me :", me, "maps :", maps[y][x], "cnt :", cnt, "next[서] :", [x+y for x,y in zip(me, [-1, 0])])
    recur(maps, [x+y for x,y in zip(me, [-1, 0])], n, m, cnt+1, route)

def solution(maps):
    # n : x좌표 최댓값, m : y좌표 최댓값
    n = len(maps[0]) - 1
    m = len(maps) - 1
    # 상대방 진영이 바로 막혀 있는 경우
    if check_blocked(maps, n, m) == True:
        return -1
    # route = deque()
    # print(n, m)
    recur(maps, [0, 0], n, m, 1, route = [])
    # 상대방 진영이 막혀 있는 경우
    if min_route == 10000:
        return -1
    return min_route



# DFS로 풀었지만 효율성 테스트 fail
from collections import deque

def solution(maps):
    # 남 > 동 > 북 > 서
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    depth = 1
    n, m = len(maps[0])-1, len(maps)-1
    route = deque()
    route.append([[0,0], depth])
    visited = []
    while route:
        node = route.popleft()
        # print("route", list(route), "visited", list(visited), "node", node[0], "depth", node[1])
        # 처음 방문한 경우
        if node[0] not in visited:
            visited.append(node[0])
            depth = node[1]
            # 적 팀 진영 도착 시 depth 리턴 (node[1])
            if node[0] == [n, m]:
                return node[1]
            # 연결될 수 있는 좌표 판단해서, route에 삽입하기
            for direction in directions:
                x = node[0][0] + direction[0]
                y = node[0][1] + direction[1]
                if x > n or x < 0 or y > m or y < 0:
                    continue
                if maps[y][x] == 1:
                    route.append([[x, y], depth+1])
    return -1