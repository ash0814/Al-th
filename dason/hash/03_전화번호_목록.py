def solution(phone_book):
    phone_book.sort()
    copy_book = phone_book
    dict_book = dict(phone_book)
    print(type(dict_book))

    for number in phone_book:
        for copy_number in copy_book:
            if number == copy_number:
                continue
            if copy_number.startswith(number):
                return False
    return True


if __name__ == '__main__':
    phone_book = ["119", "97674223", "1195524421"]
    answer = False
    if solution(phone_book) == answer:
        print("OK")
    else:
        print("KO")
