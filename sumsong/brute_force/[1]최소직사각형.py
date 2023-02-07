def solution(sizes):
    for size in sizes:
        if size[0] < size[1]:
            tmp = size[0]
            size[0] = size[1]
            size[1] = tmp
    max_width = max(sizes, key=lambda x:x[0])[0]
    max_length = max(sizes, key=lambda x:x[1])[1]
    return max_width * max_length