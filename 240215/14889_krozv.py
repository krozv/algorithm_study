# 스타트와 링크
import itertools
import sys
input = sys.stdin.readline
"""
총 N명, N은 짝수
N/2명으로 이루어짐 -> 스타트 팀 vs 링크 팀
i번 사람 + j번 사람 = Sij(능력치)
능력치가 최소가 되어야함
능력치의 최솟값을 출력하라
"""

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr_sum = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        arr_sum[i][j] = arr[j][i] + arr[i][j]

num = list(range(N))
team_list = list(itertools.combinations(num, N//2))
start = 0
end = len(team_list)-1
min_val = 1e5
for i in range(len(team_list)//2):
    s1 = list(itertools.combinations(team_list[start], 2))
    s2 = list(itertools.combinations(team_list[end], 2))
    start += 1
    end -= 1
    ss1 = 0
    ss2 = 0
    for s in range(len(s1)):
        i, j = s1[s]
        ss1 += arr_sum[i][j]
        i, j = s2[s]
        ss2 += arr_sum[i][j]
    if min_val > abs(ss1-ss2):
        min_val = abs(ss1-ss2)
print(min_val)