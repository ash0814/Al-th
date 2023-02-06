import heapq

def solution(genres, plays):
    answer = []
    album = {}
    gen = {}
    for i in range(len(genres)):
        if genres[i] in album:
            heapq.heappush(album[genres[i]], (-plays[i], i))
            gen[genres[i]] += plays[i]
        else:
            album[genres[i]] = []
            heapq.heappush(album[genres[i]], (-plays[i], i))
            gen[genres[i]] = plays[i]
    gen = dict(sorted(gen.items(), key=lambda x:x[1], reverse=True))
    for g in gen:
        if len(album[g]) > 1:
            answer.append(heapq.heappop(album[g])[1])
            answer.append(heapq.heappop(album[g])[1])
        else:
            answer.append(heapq.heappop(album[g])[1])
    return answer