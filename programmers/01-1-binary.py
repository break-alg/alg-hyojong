# 이진 변환 반복하기
# Level 2
# https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    answer = [0, 0] # 이진변환 횟수, 제거된 0의 개수
    
    while s != "1":
        answer[1] += s.count("0")   # 0 개수 카운트
        s = s.replace("0", "")      # 0 제거
        x = format(len(s), 'b')     # 0 제거된 s의 길이를 이진변환
        s = str(x)
        answer[0] += 1              # 이진변환 횟수 카운트
    
    return answer