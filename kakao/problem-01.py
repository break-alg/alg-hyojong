# 비밀 지도 (★)
# 2개의 비밀지도를 합치는 문제
# [파이썬 알고리즘 인터뷰 | p.682] 참조

def solution(n, arr1, arr2):
    map = []
    for i in range(n):
        map.append(bin(arr1[i] | arr2[i])[2:].zfill(n).replace('0', " ").replace('1', "#"))
    return map


if __name__ == '__main__':
    n = 5
    arr1 = [9, 20, 28, 18, 11]
    arr2 = [30, 1, 21, 17, 28]

    print(solution(n, arr1, arr2))