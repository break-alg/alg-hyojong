# 캐시
# 도시 이름을 입력받아 DB에서 결과를 가져오는데 성능을 개선하는 문제
# 파이썬의 데크를 사용하여 간단하게 구현한 문제
# 라이브러리 없이 다른 언어에서 구현하려면 꽤 복잡해짐
# [파이썬 알고리즘 인터뷰 | p.688] 참조
import collections


def solution(cacheSize, cities):
    answer = 0
    cache = collections.deque(maxlen=cacheSize)

    for city in cities:
        city = city.lower()
        # 캐시 히트 시 재삽입 정리
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:   # 캐시 미스 시 삽입만
            cache.append(city)
            answer += 5

    return answer


if __name__ == '__main__':
    cacheSize = 3
    cities = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']

    print(solution(cacheSize, cities))