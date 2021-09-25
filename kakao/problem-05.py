# 뉴스 클러스터링
# 두 문자열의 집합을 구한뒤 교집합과 합집합을 구하여 계산하는 문제
# collections, re 라이브러리를 잘 알아야 쉽게 구현할 수 있을거 같음
# [파이썬 알고리즘 인터뷰 | p.695] 참조
import collections
import re


def solution(str1, str2):
    answer = 0

    # 두 글자씩 끊어서 다중 집합 구성
    str1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if re.findall('[a-z]{2}', str1[i:i+2].lower())]
    str2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if re.findall('[a-z]{2}', str2[i:i+2].lower())]

    # 교집합 계산
    intersection = sum((collections.Counter(str1) & collections.Counter(str2)).values())

    # 합집합 계산
    union = sum((collections.Counter(str1) | collections.Counter(str2)).values())

    # 분모가 0인 경우는 유사도 1을 반환, 그 외에는 유사도 계산 * 65536
    answer = 1 if union == 0 else int((intersection / union) * 65536)

    return answer


if __name__ == '__main__':
    str1 = 'FRANCE'
    str2 = 'french'

    print(solution(str1, str2))