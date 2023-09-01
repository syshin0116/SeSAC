import sys
from pprint import pprint

sys.stdin = open('01_Hashing_report_result.txt')

n = int(input())

for case in range(n):
    n, m, k = map(int, input().split())
    name_list = input().split()
    matrix = []

    matrix = [input().split() for _ in range(m)]
    pprint(matrix)
    print()
    for reporter, reported in matrix:
        print(f"{reporter}가 {reported}를 신고했어요!")
    print()