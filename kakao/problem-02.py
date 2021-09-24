# 다트 게임
# 문자열로 구성된 다트 점수를 계산하는 문제
# [파이썬 알고리즘 인터뷰 | p.685] 참조

def solution(dartResult):
    nums = [0]
    for d in dartResult:
        if d == 'S':
            nums[-1] **= 1
            nums.append(0)
        elif d == 'D':
            nums[-1] **= 2
            nums.append(0)
        elif d == 'T':
            nums[-1] **= 3
            nums.append(0)
        elif d == '*':
            nums[-2] *= 2
            if len(nums) > 2:
                nums[-3] *= 2
        elif d == '#':
            nums[-2] *= -1
        else:
            nums[-1] = nums[-1] * 10 + int(d)

    return sum(nums)


if __name__ == '__main__':
    dartResult = '1S2D*3T'

    print(solution(dartResult))