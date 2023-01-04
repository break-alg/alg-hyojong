# 숫자의 표현
# Level 2
# https://school.programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    answer = 0
    
    # 1부터 n까지 하나씩 시작
    for i in range(1, n + 1):
        num = n
        # i부터 연속되는 수 빼기
        for j in range(i, n + 1):
            num -= j
            # 결과가 0 이하일 경우 반복문 탈출
            if num < 1:
                break
        # 뺀 결과가 최종 0일 경우 조건 만족
        if num == 0:
            answer += 1
    
    return answer