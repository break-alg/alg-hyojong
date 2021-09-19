# 너비 우선 탐색(Breadth First Search) 구현
# 다익스트라 알고리즘에서 유용하게 사용
#
# 반복과 큐를 사용한 BFS
def iterative_bfs(graph, start_v):
    discovered = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered


graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3]
}

print(iterative_bfs(graph, 1))