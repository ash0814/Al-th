# DFS로 풀었는데 효율성 테스트 fail
from collections import deque

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