# 서로 다른 문자열의 개수
# exhaustive method - 시간 초과
"""
import sys
input = sys.stdin.readline
string = input()
str_list = []
for n in range(1, len(string)+1):       # 문자열의 길이
    for i in range(len(string)-n+1):    # 문자열 시작점
        sub = string[i:i+n]
        if sub not in str_list:         # 문자열이 리스트 안에 없을 경우에만 append
            str_list.append(sub)
print(len(str_list))
"""
# 또초과
"""
import sys
input = sys.stdin.readline
string = input().rstrip('\n')
str_list = []
for n in range(1, len(string)+1):       # 문자열의 길이
    for i in range(len(string)-n+1):    # 문자열 시작점
        sub = string[i:i+n]
        if sub not in str_list:         # 문자열이 리스트 안에 없을 경우에만 append
            str_list += [sub]
print(len(str_list))
"""
# 어떻게 해야 시간초과가 안날까? 머리를 굴려보자!
# 스택 사용해보기  X  -> KMP algorithm이었나? -> 그냥 dictionary 사용
import sys
input = sys.stdin.readline
string = input().rstrip('\n')
str_dict = {}
for n in range(1, len(string)+1):
    for i in range(len(string)-n+1):
        sub = string[i:i + n]
        if not str_dict.get(sub):
            str_dict[sub] = 1
print(len(str_dict))

