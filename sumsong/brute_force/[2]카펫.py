def solution(brown, yellow):
    # 방정식
    # brown = (height * 2) + (width * 2) - 4
    # brown = 2width + 2height - 4
    # yellow = (width - 2) * (height - 2)
    # yellow = width*height - 2height -2width + 4
    
    # 연립으로 도출한 조건식 2개
    # yellow + brown = width * height
    # brown = 2height + 2width - 4
    
    for width in range((brown + yellow) // 2, 2, -1):
        height = 0
        if (brown + yellow) % width == 0:
            height = (brown + yellow) // width
        if brown == (2 * height + 2 * width - 4) and width >= height and height > 2:
            return [width, height]