# 자료형, 변수

# 변수, 할당

name = 'jun'

# 동시할당

x, y = 10, 20
print(x, y)

# x와 y 바꾸는 방법
x, y = y, x
print(x, y)

# 연산자
    # 산술연산자
    # 복합연산자
    # 논리연산자

# 연산 우선순위

nums = [1, 2, 3, 4, 5]
num = 6

if num in nums == False:
    print(0)
else:
    print(1)

# 우선순위가 동일함으로
# if (num in nums) and (nums == False): 와 동일하게 작동한다

# 단축평가
# and나 or 조건에서 이미 앞에서 결정이 나면 뒤 연산은 작동하지 않는다

print(5 or 0)  # 5
print(5 and 0)  # 0
print(0 or 5)  # 5

nums = [1,2,3,4]
while nums:
    num = nums.pop()
    print(num)

# 컨테이너, 자료구조

# 리스트, 딕셔너리, 튜플, 문자열, 레인지, 집합

# 순서가 있는지(iterable)
    # 순서가 있는: 리스트, 튜플, 문자열,레인지
    # 순서가 없는: 집합, 딕셔너리

# 튜플
import numpy as np
my_lst = [1, 2, 3]
my_tuple = (1, 2, 3)

print(my_tuple)


# 조건문
# if 조건문:
#     동작2
#     동작1
# elif 조건문2:
#     동작3
# else:
#     동작4


# foreach와 for range 비교:
# index로 접근 시 원본 리스트를 변경할 수 있지만, foreach의 경우 불가능하다


# 함수

# 선언
# def 함수이름(매개변수):
#     동작

# 호출