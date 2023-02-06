def solution(phone_book):
    book = {}
    for number in phone_book:
        if book.get(number[0]):
            book[number[0]].append(number)
        else:
            book[number[0]] = [number]
    for key, value in book.items():
        # print(key, value)
        if len(value) >= 2:
            value.sort()
            for i in range(len(value) - 1):
                if value[i] == value[i+1][:len(value[i])]:
                    return False
    return True