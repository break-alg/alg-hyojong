# 깊이 우선 탐색(Depth First Search) 구현
#
# 재귀 함수 사용한 DFS
def recursive_dfs(graph, v, discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if not w in discovered:
            discovered = recursive_dfs(graph, w, discovered)
    return discovered


# 반복과 스택을 사용한 DFS
def iterative_dfs(start_v):
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
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

print(recursive_dfs(graph, 1))
print(iterative_dfs(1))

# 출력 결과
# [1, 2, 5, 6, 7, 3, 4]
# [1, 4, 3, 5, 7, 6, 2]
#
# 출력 결과가 다른 이유는 stack을 사용할 때 LIFO 방식이기 때문에
# 재귀와는 반대로 시작하기 때문