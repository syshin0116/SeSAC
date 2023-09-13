lst = [9, 3, 7, 2, 5, 8, 11, 6]


def partition(low, high):
    pivot = lst[high]
    left = low
    for right in range(low, high):
        if lst[right] < pivot:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
    lst[left], lst[high] = lst[high], lst[left]

    return left


def lomuto(low, high):
    if low < high:
        pivot = partition(low, high)
        lomuto(low, pivot - 1)
        lomuto(pivot + 1, high)

lst = [9, 3, 7, 2, 5, 8, 11, 13]


def hoare_partition(low, high):
    pivot = (low+high)//2
    l = low
    r = high
    while l < r:
        while lst[l] < lst[pivot] and l < r:
            l += 1
        while lst[r] > lst[pivot] and l < r:
            r -= 1
        if l < r:
            lst[l], lst[r] = lst[r], lst[l]

def hoare(low, high):
    if low < high:
        pivot = hoare_partition(low, high)
        hoare(low, pivot-1)
        hoare(pivot+1, high)


hoare(0, len(lst)-1)
print(lst)