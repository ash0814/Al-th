def solution(citations):
    h_index = 0
    citations.sort(reverse=True)
    print(citations)
    try:
        for index in range(len(citations) + 1):
            if citations[index] == index:
                return citations[index]
            if citations[index] < index:
                h_index = index
                break
    except:
        return len(citations)
    return h_index


if __name__ == '__main__':
    citations = [3, 0, 6, 1, 5]
    answer = 3
    if solution(citations) == answer:
      print("Ok")
    else:
        print("KO")
