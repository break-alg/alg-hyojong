# 다음 큰 숫자
# Level 2
# https://school.programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    answer = 0
    
    p_one = str(format(n, 'b'))
    p_one_count = p_one.count('1')
    
    for i in range(n + 1, 1000001):
        i_one = str(format(i, 'b'))
        i_one_count = i_one.count('1')
        if p_one_count == i_one_count:
            answer = i
            break
    
    return answer