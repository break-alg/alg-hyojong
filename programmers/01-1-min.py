# 최소값 만들기
# Level 2
# https://school.programmers.co.kr/learn/courses/30/lessons/12941

def solution(A,B):
    answer = 0

    # A에서 가장 작은 값과 B에서 가장 큰 값을 곱한 값들의 합이 최소값
    # A -> 오름차순 정렬
    # B -> 내림차순 정렬
    A.sort()
    B.sort(reverse=True)
    
    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer