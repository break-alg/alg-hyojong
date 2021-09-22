# 버블 정렬
# O(n^2)이라 잘 안씀

def bubblesort(A):
    for i in range(1, len(A)):
        for j in range(0, len(A) - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    return A

if __name__ == "__main__":
    nums = [1, 6, 2, 5, 3, 11, 4, 0]
    print(bubblesort(nums))