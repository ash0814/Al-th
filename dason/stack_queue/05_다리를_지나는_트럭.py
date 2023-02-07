from collections import deque


def solution(bridge_length, weight, truck_weights):
    result = 0
    d = deque()
    for index in range(bridge_length):
        d.append(0)
    total_weight = 0
    while truck_weights:
        result += 1
        total_weight -= d[0]
        d.popleft()

        total_weight += truck_weights[0]
        if total_weight <= weight:
            d.append(truck_weights[0])
            del truck_weights[0]
        else:
            total_weight -= truck_weights[0]
            d.append(0)
    return result + bridge_length


if __name__ == '__main__':
    bridge_length = 100
    weight = 100
    truck_weights = [10,10,10,10,10,10,10,10,10,10]
    answer = 110
    if solution(bridge_length, weight, truck_weights) == answer:
        print("OK")
    else:
        print("KO")