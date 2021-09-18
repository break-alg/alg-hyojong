# 네이버 웹툰 인턴
# 라이브 코딩 테스트 문제
# 스택 2개를 사용하여 큐 구현
class StackToQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, item):
        self.input.append(item)

    def pop(self):
        self.peek()
        return self.output.pop()

    def peek(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self):
        return self.input == [] and self.output == []