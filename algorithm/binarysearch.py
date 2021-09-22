# 이진 탐색
#
# 재귀를 사용한 이진 탐색
def recursive_search(nums, target, left, right):
    if left <= right:
        mid = (left + right) // 2

        if nums[mid] < target:
            return recursive_search(nums, target, mid + 1, right)
        elif nums[mid] > target:
            return recursive_search(nums, target, left, mid - 1)
        else:
            return mid
    else:
        return -1


def iterative_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9

    print(recursive_search(nums, target, 0, len(nums) - 1))
    print(iterative_search(nums, target))