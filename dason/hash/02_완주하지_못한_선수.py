def solution(participant, completion):
    participant.sort()
    completion.sort()
    for index, name in enumerate(participant):
        if index >= len(completion):
            return name
        if name != completion[index]:
            return name

if __name__ == '__main__':
    participant = ["leo", "kiki", "eden"]
    completion = ["eden", "kiki"]
    answer = "leo"

    if solution(participant, completion) == answer:
        print("OK")
    else:
        print("KO")
