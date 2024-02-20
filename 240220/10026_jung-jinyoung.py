import sys
sys.setrecursionlimit(100000)


# 영역을 알아낼 수 있도록 dfs 함수 작성
def dfs(x, y, color, is_blindness):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            if not is_blindness: # 적록색약 X
                if board[nx][ny] == color:
                    visited[nx][ny] = 1
                    dfs(nx, ny, color, is_blindness)
            else: # 적록색약 O
                if color == 'R' or color == 'G':
                    if board[nx][ny] == 'R' or board[nx][ny] == 'G':
                        visited[nx][ny] = 1
                        dfs(nx, ny, color, is_blindness)
                else:
                    if board[nx][ny] == color:
                        visited[nx][ny] = 1
                        dfs(nx, ny, color, is_blindness)

n = int(input())
board = [list(input().rstrip()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

count = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]: # 이미
            visited[i][j] = 1
            dfs(i, j, board[i][j], 0)
            count += 1

print(count, end=' ')

visited = [[0] * n for _ in range(n)] #  초기화
count = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = 1
            dfs(i, j, board[i][j], 1)
            count += 1

print(count)
