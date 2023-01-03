# JadenCase 문자열 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12951#

def solution(s):
    answer = ''

    word = ''       # 단어를 표시할 변수

    # 문자열 길이만큼 반복
    for i in range(len(s)):
        # 공백을 만날 경우 단어 처리 
        if s[i] == ' ':
            answer += word[:1].upper() + word[1:].lower() + ' '
            word = ''
        # 공백이 아닌 문자일 경우 단어 변수에 저장
        else:
            word += s[i]
    
    # 마지막 단어 처리
    answer += word[:1].upper() + word[1:].lower() 
    
    return answer