def solution(clothes):
    result = 0
    dic = dict()
    for cloth in clothes:
        if cloth[1] in dic:
            dic[cloth[1]] = dic.get(cloth[1]) + 1
        else:
            dic[cloth[1]] = 2
    if len(dic) != 1:
        comb = 1
        print(dic.values())
        for key in dic.keys():
            comb *= dic.get(key)
        result += comb
    print(result)
    return result - 1


if __name__ == '__main__':
    clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
    answer = 5
    if solution(clothes) == answer:
        print("OK")
    else:
        print("KO")
