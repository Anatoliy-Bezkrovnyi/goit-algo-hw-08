import heapq

cables_length = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]

heapq.heapify(cables_length)

while len(cables_length) != 1:
    min_1 = heapq.heappop(cables_length) 
    min_2 = heapq.heappop(cables_length)
    sum_min = min_1 + min_2
    heapq.heappush(cables_length, sum_min)
    print(cables_length)