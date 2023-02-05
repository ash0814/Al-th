from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    sum_weight = 0
    bridge = deque([0 for i in range(bridge_length)])
    while truck_weights:
        pop_truck = bridge.popleft()
        sum_weight -= pop_truck
        if sum_weight + truck_weights[0] <= weight:
            truck = truck_weights.pop(0)
            bridge.append(truck)
            sum_weight += truck
        else:
            bridge.append(0)
        answer += 1
    answer += len(bridge)
    return answer