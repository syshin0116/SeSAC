n = 5

# 세로
dx = [0, 1, 0, -1]
# 가로
dy = [1, 0, -1, 0]

snail = [[0]*n for _ in range(n)]

x, y = 0, 0
d = 0
for num in range(1, n**2 + 1):
    print(x, y, num)
    snail[x][y] = num

    # x, y 라는 녀석들을 이동
    nx = x + dx[d]
    ny = y + dy[d]

    # nx, ny가 그리드를 벗어난 순간에는 방향 변경
    if nx < 0 or nx >= n or ny < 0 or ny >= n or snail[nx][ny]:
        d = (d + 1)%4
        nx = x + dx[d]
        ny = y + dy[d]


    x, y = nx, ny

    for i in snail:
        print(i)
    print()