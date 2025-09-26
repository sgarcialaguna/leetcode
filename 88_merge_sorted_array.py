from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    i = m - 1
    k = n - 1
    for j in range(m + n - 1, -1, -1):
        if i < 0:
            nums1[j] = nums2[k]
            k -= 1
        elif k < 0:
            break
        elif nums2[k] > nums1[i]:
            nums1[j] = nums2[k]
            k -= 1
        else:
            nums1[j] = nums1[i]
            i -= 1


merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
merge([1], 1, [], 0)
merge([0], 0, [1], 1)
