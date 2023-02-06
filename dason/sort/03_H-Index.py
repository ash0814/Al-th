def solution(citations):
    h_index = 0
    citations.sort(reverse=True)
    try:
        for index in range(len(citations) + 1):
            print(index, citations[index])
            if citations[index] == index:
                return citations[index]
            if citations[index] < index:
                h_index = index
                if citations[index] == 0:
                    return 0
                break
    except:
        return len(citations)
    return h_index


if __name__ == '__main__':
    citations = [0, 0, 0]
    answer = 0
    if solution(citations) == answer:
      print("Ok")
    else:
        print("KO")
