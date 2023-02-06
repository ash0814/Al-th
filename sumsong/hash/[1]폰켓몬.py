def solution(nums):
    count = len(nums)
    monster_ball = {}
    for pokemon in nums:
        if pokemon in monster_ball:
            monster_ball[pokemon] += 1
        else:
            monster_ball[pokemon] = 1
    if count / 2 < len(monster_ball):
        return count / 2
    return len(monster_ball)
