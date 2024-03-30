# 17825_bj(주사위 윷놀이)
'''
https://www.acmicpc.net/problem/17825
https://velog.io/@yoonuk/%EB%B0%B1%EC%A4%80-17825-%EC%A3%BC%EC%82%AC%EC%9C%84-%EC%9C%B7%EB%86%80%EC%9D%B4-Python
이 블로그 참고해서 풀었음
다시 풀어보기
하드코딩 하는게 별로인게 아닌듯
'''
graph = [[1], [2], [3], [4], [5],
         [6, 21], [7], [8], [9], [10],
         [11, 25], [12], [13], [14], [15],
         [16, 27], [17], [18], [19], [20],
         [32], [22], [23], [24], [30],
         [26], [24], [28], [29], [24],
         [31], [20], [32]]

score = [0, 2, 4, 6, 8,
         10, 12, 14, 16, 18,
         20, 22, 24, 26, 28,
         30, 32, 34, 36, 38,
         40, 13, 16, 19, 25,
         22, 24, 28, 27, 26,
         30, 35, 0]

def back(d, s, h):
    global result
    if d >= 10:
        result = max(result, s)
        return

    for i in range(4):
        x = h[i]

        if len(graph[x]) == 2:
            x = graph[x][1]
        else:
            x = graph[x][0]

        for _ in range(1, dice[d]):
            x = graph[x][0]

        if x == 32 or (x < 32 and x not in h):
            before = h[i]
            h[i] = x
            back(d+1, s + score[x], h)
            h[i] = before

dice = list(map(int, input().split()))
result = 0
back(0,0,[0,0,0,0])
print(result)