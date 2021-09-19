# 최단 경로 문제를 다익스트라 알고리즘을 사용하여 해결
# 다익스트라의 경우 BFS를 사용하기 때문에 BFS 알고리즘을 변형하여 구현
# 확실히 이해 힘듬... 좀 더 공부 요망...
import collections
import heapq


def networkDelayTime(times, N, K):
    graph = collections.defaultdict(list)

    # 그래프 인접 리스트 구성
    for u, v, w in times:
        graph[u].append((v, w))

    # 큐 변수: [(소요 시간, 정점)]
    Q = [(0, K)]
    dist = collections.defaultdict(int)

    # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for v, w, in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))

    # 모든 노드의 최단 경로 존재 여부 판별
    if len(dist) == N:
        return max(dist.values())
    return -1


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
N = 4
K = 3

print(networkDelayTime(times, N, K))
