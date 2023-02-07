def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            print(temp)
            print(hash_map)
            print(temp in hash_map)
            print(phone_number)
            print()
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer


if __name__ == '__main__':
    phone_book = ["119", "97674223", "1195524421"]
    answer = False
    if solution(phone_book) == answer:
        print("OK")
    else:
        print("KO")
