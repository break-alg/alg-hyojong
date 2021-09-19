# 이진 트리의 최대 깊이 문제
# 이진 트리 깊이는 BFS로 탐색하며 구할 수 있음
# while 반복문이 돌아간 횟 수에 따라 깊이 측정 가능
import collections


def maxDepth(root):
    if root is None:
        return 0

    queue = collections.deque([root])
    depth = 0

    while queue:
        depth += 1
        # 큐 연산 추출 노드의 자식 노드 삽입
        for _ in range(len(queue)):
            cur_root = queue.popleft()
            if cur_root.left:
                queue.append(cur_root.left)
            if cur_root.right:
                queue.append(cur_root.right)

    # BFS 반복 횟수 == 깊이
    return depth