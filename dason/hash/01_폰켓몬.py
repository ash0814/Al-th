def solution(nums):
    result = 0
    pocket = set()
    pocket_max = len(nums) / 2
    for num in nums:
        pocket.add(num)
    if len(pocket) < pocket_max:
        result = len(pocket)
    else:
        result = pocket_max
    return result


if __name__ == '__main__':
    nums = [3,3,3,2,2,4]
    answer = 3
    if solution(nums) == answer:
        print("OK")
    else:
        print("KO")

