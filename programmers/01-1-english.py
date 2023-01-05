# 영어 끝말잇기
# Level 2
# https://school.programmers.co.kr/learn/courses/30/lessons/12981

import math 

def solution(n, words):
    answer = [0, 0]

    l = {}
    
    l[words[0]] = 1    
    for i in range(1, len(words)):
        if words[i] in l or words[i-1][-1] != words[i][0] or len(words[i]) < 2:
            answer[1] = math.ceil((i + 1) / n)
            answer[0] = (i % n) + 1
            break
        else:
            l[words[i]] = 1
            
    return answer