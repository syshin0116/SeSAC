# 정렬
# 시간 복잡도에 따른 종류:
# O(n^2): 버블정렬,
# O(n):
# O(nlogn): 퀵정렬, 힙정렬
# 팀정렬: 퀵정렬+힙정렬

arr = [6, 3, 7, 2, 5, 8, 11, 13]

def merge_sort(lst):
    if len(lst) == 1:
        return lst
    mid = len(lst)//2
    left_half = lst[:mid]
    right_half = lst[mid:]

    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    return merge(left_sorted, right_sorted)


def merge(left, right):
    l = 0
    r = 0
    idx = 0

    result = [0] * (len(left) + len(right))
    print(left, right)
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result[idx] = left[l]
            l += 1
            idx += 1
        else:
            result[idx] = right[r]
            r += 1
            idx += 1
    # if l < len(left):
    #     result = result[:-l]
    #     result.extend(left[:l])
    #
    # while l < len(left):
    #     result

    return result

print(merge_sort(arr))