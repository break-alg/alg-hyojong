# 그리디 알고리즘
# 배낭 15kg 일 때, 가치($)의 합이 최대가 되도록 하는 방법 찾기
# 아래 풀이는 무게를 쪼갤 수 있을 경우만 가능
def greed(cargo):
    capacity = 15
    pack = []
    w = []
    # 단가 계산 역순 정렬
    for c in cargo:
        pack.append((c[0] / c[1], c[0], c[1]))
    pack.sort(reverse=True)
    print(pack)
    # 단가 순 그리디 계산
    total_value: float = 0
    for p in pack:
        if capacity - p[2] >= 0:
            w.append(p[2])
            capacity -= p[2]
            total_value += p[1]
        else:
            fraction = capacity / p[2]
            w.append(fraction * p[1])
            total_value += p[1] * fraction
            break
    print(w)
    return total_value


if __name__ == '__main__':
    cargo = [
        (4, 12),
        (2, 1),
        (10, 4),
        (1, 1),
        (2, 2),
    ]

    print(greed(cargo))