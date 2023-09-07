n = 3
lst = []

counting_lst = [0] * (n + 1)

for i in lst:
    counting_lst[i] += 1

print(counting_lst)
old_counting_lst = counting_lst[:]

for i in range(1, len(counting_lst)):
    counting_lst[i] = counting_lst[i + counting_lst[i-1]]

print(counting_lst)

lst = [0, 1, 3, 4, 2, 2, 1, 0, 1]

# 거꾸로 반복을 돌 예정
# 1. 리스트를 뒤집어서 반복을 돌 수 있다

sorted_lst = [0]*len(lst)
for num in lst[::-1]:
    put_index = counting_lst[num] - 1
    sorted_lst[put_index] = num

    counting_lst[num] = counting_lst[num] - 1

print(sorted_lst)
