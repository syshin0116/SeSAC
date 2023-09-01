import sys
from pprint import pprint

sys.stdin = open('input2.txt')

n = int(input())

matrix = []
for _ in range(n):
    name, num = list(input().split())
    matrix.append([name, int(num)])

pprint(matrix)
