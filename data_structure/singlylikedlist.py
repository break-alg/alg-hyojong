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

    def append(self, item):
        if self.size == 0:
            self.head = Node(item, None)
            self.size += 1
        else:
            node = self.head
            while node.next != None:
                node = node.next
            node.next = Node(item, None)
            self.size += 1

    def insertAtIndex(self, item, index):
        if self.size == 0:
            print("List is empty!!")
        elif 0 > index or index > self.size:
            print("Wrong index!!")
        elif index == 0:
            nNode = Node(item, self.head)
            self.head = nNode
            self.size += 1
        else:
            pNode = self.head
            for i in range(1, self.size + 1):
                if i == index:
                    nNode = Node(item, pNode.next)
                    pNode.next = nNode
                    self.size += 1
                    break
                pNode = pNode.next

    def remove(self, index):
        if self.size == 0:
            print("List is empty!!")
        elif 0 > index or index > self.size - 1:
            print("Wrong index!!")
        elif index == 0:
            rNode = self.head
            self.head = rNode.next
            self.size -= 1
        else:
            pNode = self.head
            for i in range(1, self.size):
                rNode = pNode.next
                if i == index:
                    pNode.next = rNode.next
                    self.size -= 1
                    break
                pNode = rNode

    def searchIndex(self, item):
        index = -1

        if self.size == 0:
            print("List is empty!!")
        else:
            node = self.head
            for i in range(0, self.size):
                if node.item == item:
                    index = i
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

if __name__ == "__main__":
    sl = SinglyLinkedList()
    sl.append(1)
    sl.append(2)
    sl.append(3)
    sl.print()
    print()
    sl.remove(0)
    sl.remove(2)
    sl.print()
    print()
    sl.insertAtIndex(3, 1)
    sl.insertAtIndex(0, 3)
    sl.print()
    print(sl.getItem(3))
    print(sl.searchIndex(0))
    sl.clear()
    sl.print()