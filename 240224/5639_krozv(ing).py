# 5639. 이진 검색 트리
"""
왼쪽: 최대힙
오른쪽: 최소힙
전위 순회한 결과를 후위 순회로 변환
"""
import sys
input = sys.stdin.readline
num = []
while True:
    try:
        num.append(int(input()))
    except:
        break
print(num)