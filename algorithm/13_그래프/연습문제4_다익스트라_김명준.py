import heapq

# s: 시작 정점, A: 인접행렬, D: 거리
def Dijkstra(s, A, D):
    # U: 선택된 정점 집합
    U = [inf]*6
    U[s] = 0

    for v in range(len(U)):
        D[v] = arr[s][v]



# h = []
# heapq.heappush(h, (3, 'good'))
# heapq.heappush(h, (10, "Do not study"))
# print(h)

inf = 10000000
arr = [
    [0, 3, 4, inf, inf, inf],
    [inf, 0, inf, 5, inf, inf],
    [inf, 1, 0, 4, 5, inf],
    [inf, inf, inf, 0, 3, 4],
    [3, inf, inf, inf, 0, 5],
    [inf, inf, inf, inf, inf, inf],
]

Dijkstra(0, arr, [0]*6)