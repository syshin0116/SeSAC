# url: https://www.acmicpc.net/problem/2178
from pprint import pprint


def solution(input):
    matrix = []
    for idx, i in enumerate(input.split('\n')):
        if idx == 0:
            size = i
        else:
            matrix.append(list(map(int, )))
    pprint(matrix)


if __name__ == '__main__':
    solution('''3
ken 2
jun 3
alex 10''')


# input text1
# 4 3
# 1 2 3
# 4 5 6
# 7 8 9
# 10 11 12


# input text2
# 3
# ken 2
# jun 3
# alex 10