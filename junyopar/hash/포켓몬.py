def solution(nums):
    answer = 0
    num_list = []
    # for i in nums:
    #     if i not in num_list:
    #         num_list.append(i)
    num_list = set(nums)
    if len(nums)//2 <= len(num_list):
        return len(nums)//2
    if len(nums)//2 > len(num_list):
        return len(num_list)
        
  # 와 set이 개빠르긴 하네 
    # for 문으로 넣어주는건 229ms 걸리는것도 있는데 ..