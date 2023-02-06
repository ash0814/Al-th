def solution(s):
    result = True
    l = []
    for c in s:
        if c == '(':
            l.append(c)
        else:
            if l == []:
                return False
            l.pop()
    if l == []:
        return True
    else:
        return False


if __name__ == '__main__':
    s = "()()"
    answer = True
    if solution(s) == answer:
        print("OK")
    else:
        print("KO")
