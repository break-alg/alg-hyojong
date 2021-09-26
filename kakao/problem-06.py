# 프렌즈 4블록
# 2 X 2 형태의 블록을 지우는 게임 구현
# 어려운 문제는 아니나, 구현해야할 로직이 많아 매우 복잡함
# [파이썬 알고리즘 인터뷰 | p.699] 참조

def solution(m, n, board):
    answer = 0
    board = [list(x) for x in board]

    matched = True
    while matched:
        # 1) 매치 여부 판별
        matched = []
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1] != '#':
                    matched.append([i, j])

        # 2) 일치한 위치 삭제
        for i, j in matched:
            board[i][j] = board[i][j+1] = board[i+1][j] = board[i+1][j+1] = '#'

        # 3) 빈공간 블럭 처리
        for _ in range(m):
            for i in range(m - 1):
                for j in range(n):
                    if board[i+1][j] == '#':
                        board[i+1][j], board[i][j] = board[i][j], '#'

    answer = sum(x.count('#') for x in board)

    return answer


if __name__ == '__main__':
    m = 4
    n = 5
    board = ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']

    print(solution(m, n, board))