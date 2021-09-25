# 셔틀버스
# [파이썬 알고리즘 인터뷰 | p.6691] 참조
def solution(n, t, m, timeTable):
    answer = ''

    timeTable = [int(time[:2]) * 60 + int(time[:2]) for time in timeTable]
    timeTable.sort()

    current = 540

    for _ in range(n):
        for _ in range(m):
            # 대기가 있는 경우 1초 전 도착
            if timeTable and timeTable[0] <= current:
                candidate = timeTable.pop() - 1
            else:
                candidate = current
        current += t

    h, m = divmod(candidate, 60)
    answer = str(h).zfill(2) + ':' + str(m).zfill(2)
    return answer


if __name__ == '__main__':
    n = 1
    t = 1
    m = 5
    timeTable = ['08:00', '08:01', '08:02', '08:03']

    print(solution(n, t, m, timeTable))