from collections import deque


def solution(bridge_length, weight, truck_weights):
    result = 0
    d = deque()
    d.append(0)
    d.append(0)
    while truck_weights:
        result += 1
        if len(d) >= 1:
            d.popleft()
        total_weight = 0
        while truck_weights:
            print(truck_weights[0])
            if len(d) < bridge_length and total_weight < weight:
                d.append(truck_weights[0])
                total_weight += truck_weights[0]
                del truck_weights[0]
                result += 1
                print(d)
            else:
                break
    print(result)
    return result


if __name__ == '__main__':
    bridge_length = 100
    weight = 100
    truck_weights = [10,10,10,10,10,10,10,10,10,10]
    answer = 110
    if solution(bridge_length, weight, truck_weights) == answer:
        print("OK")
    else:
        print("KO")