# 동적 프로그래밍 구현
# 피보나치 수열 구하는 문제가 DP로 푸는 가장 기본적인 방식
# 반복문을 사용하는 상향식 방법과 재귀를 사용하는 하향식 방법으로 나뉨
# 편의상 딕셔너리를 사용했지만 배열로 해도 무관
import collections


def recursive_fibo(dp, N):
    if N <= 1:
        return N

    if dp[N]:
        return dp[N]

    dp[N] = recursive_fibo(dp, N - 1) + recursive_fibo(dp, N - 2)

    return dp[N]


def iterative_fibo(dp, N):
    dp[1] = 1
    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[N]


def fibo(N):
    x, y = 0, 1
    for i in range(0, N):
        x, y = y, x + y
    return x


if __name__ == '__main__':
    dp = collections.defaultdict(int)

    print(recursive_fibo(dp, 8))
    print(iterative_fibo(dp, 8))
    print(fibo(8))