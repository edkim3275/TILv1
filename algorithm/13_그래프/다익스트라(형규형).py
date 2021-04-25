inf = 10000000
arr = [
    [0, 3, 4, inf, inf, inf],
    [inf, 0, inf, 5, inf, inf],
    [inf, 1, 0, 4, 5, inf],
    [inf, inf, inf, 0, 3, 4],
    [3, inf, inf, inf, 0, 5],
    [inf, inf, inf, inf, inf, inf],
]

visited = [0] * 6
distance = [0] * 6


# 방문하지 않은 노드 중 가장 짧은 것 찾기
def small() -> int:
    min_v = inf
    index = 0
    for i in range(6):
        if distance[i] < min_v and visited[i] == 0:
            min_v = distance[i]
            index = i
    return index


def dijkstra(start: int) -> None:
    for i in range(6):
        distance[i] = arr[start][i]
    visited[start] = 1
    for i in range(4):
        current = small()
        visited[current] = 1
        for j in range(6):
            if distance[current] + arr[current][j] < distance[j]:
                distance[j] = distance[current] + arr[current][j]


dijkstra(0)
print(distance)