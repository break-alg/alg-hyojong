# 피보나치 수
# Level 2
# https://school.programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    answer = fibo(n) % 1234567
    return answer

def fibo(n):
    x = 0
    y = 1
    z = 0
    
    for i in range(2, n + 1):
        z = x + y
        x = y
        y = z
        
    return z