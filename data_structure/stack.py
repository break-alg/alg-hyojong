# 연결 리스트를 사용한 스택 구현
#
# 스택에 값을 저장할 노드 클래스
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


# 스택 클래스
class Stack:
    def __init__(self):
        self.last = None

    def push(self, item):
        self.last = Node(item, self.last)

    def pop(self):
        item = self.last.item
        self.last = self.last.next
        return item

