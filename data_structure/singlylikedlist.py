# 연결 리스트 구현
#
# 연결 리스트에 값을 저장할 노드 클래스
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


# 연결 리스트 클래스
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def firstInsert(self, item):
        if self.size == 0:
            newNode = Node(item, None)
            self.head = newNode
            self.size += 1
        else:
            newNode = Node(item, None)
            newNode.next = self.head
            self.head = newNode
            self.size += 1

    def middleInsert(self, item, index):
        if self.size == 0:
            print("List is empty!!")
        elif 0 > index > self.size:
            print("Wrong index!!")
        else:
            node = self.head
            for i in range(0, self.size):
                if i == index:
                    newNode = Node(item, node.next)
                    node.next = newNode
                    self.size += 1
                    break
                else:
                    node = node.next

    def lastInsert(self, item):
        if self.size == 0:
            print("List is empty!!")
        else:
            node = self.head
            for i in range(0, self.size):
                if i == (self.size - 1):
                    newNode = Node(item, None)
                    node.next = newNode
                    self.size += 1
                    break
                else:
                    node = node.next

    def remove(self, index):
        if self.size == 0:
            print("List is empty!!")
        elif 0 > index > self.size:
            print("Wrong index!!")
        else:
            node = self.head
            for i in range(0, self.size):
                if i == index:
                    removeNode = node
                    node
                    break
                node = node.next
        return None

    def searchIndex(self, item):
        index = -1

        if self.size == 0:
            print("List is empty!!")
        else:
            node = self.head
            for i in range(0, self.size):
                if node.item == item:
                    index = i + 1
                    break
                node = node.next

        return index

    def getItem(self, index):
        item = None

        if self.size == 0:
            print("List is empty!!")
        else:
            node = self.head
            for i in range(0, self.size):
                if i == index:
                    item = node.item
                    break
                node = node.next

        return item

    def clear(self):
        self.head = None
        self.size = 0

    def print(self):
        if self.size == 0:
            print("List is empty!!")
        else:
            node = self.head
            for i in range(0, self.size):
                print(node.item)
                node = node.next