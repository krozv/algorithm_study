# 18809_bj(Gaaaaaaaaaarden)
'''
미완성
'''
# from itertools import combinations
# import copy
#
# def select():
#     start2 = copy.deepcopy(start)
#     g_s = list(combinations(start2, g))
#     start2 = [i for i in start2 if i not in g_s]
#     r_s = list(combinations(start2, r))
#     return g_s, r_s
#
# def diffusion(start, color, red, green):
#     g_s, r_s = [], []
#     x, y = start
#     for d in [1,0], [-1,0], [0,1], [0,-1]:
#         mx = x + d[0]
#         my = y + d[1]
#         if 0 <= mx < m and 0 <= my < n and garden[my][mx] in [1, 2]:
#             if color == g and not green[my][mx]:
#                 green[my][mx] = 1
#                 g_s.append([mx, my])
#             if color == r and not red[my][mx]:
#                 red[my][mx] = 1
#                 r_s.append([mx, my])
#     return g_s, r_s
#
# def blossom():
#     global result
#     g_starts, r_starts = select()
#     for i in range(len(g_starts)):
#         g_start, r_start = g_starts[i], r_starts[i]
#         green = [[0] * m for _ in range(n)]
#         red = [[0] * m for _ in range(n)]
#         cnt = 0
#         while g_start or r_start:
#             # print(g_start, r_start)
#             for g_s in g_start:
#                 print(g_s)
#                 tmp_g = diffusion(g_s, g, green, red)
#             for r_s in r_start:
#                 tmp_r = diffusion(r_s, r, green, red)
#
#             for y in range(n):
#                 for x in range(m):
#                     if green[y][x] and red[y][x]:
#                         green[y][x] = 3
#                         red[y][x] = 3
#             g_start, r_start = tmp_g[0], tmp_r[0]
#
#         for y in range(n):
#             for x in range(m):
#                 if green[y][x]==1 and red[y][x]==1:
#                     cnt += 1
#         result = max(result, cnt)
#
# n, m, g, r = map(int, input().split())
# garden = []
# start = []
# result = 0
# for y in range(n):
#     garden.append(list(map(int, input().split())))
#     for x in range(n):
#         if garden[y][x] == 2:
#             start.append([x, y])
#
#
# blossom()
#
# print(result)