# list, queue, stack

from collections import deque, defaultdict

queue = deque()

# 여러 데이터 저장 -> 리스트
# 넣었다 뺐다 자주 -> queue, deque

# linked list

a = [1, 2, 3, 4, 5]

print(a[:3])
b = deque(a)

print(b)

# print(b[:3]) # deque는 slicing 불가능하기 떄문에 error


dic = defaultdict(int) # 존재하지 않는 딕셔너리에 연산을 하면 연산 전에 기본값을 넣어줌

dic['a'] += 1
print(dic)
