num = int(input())
line = 1

# num의 대각선 위치 찾고 싶었음
while num > line:
    num = num - line
    line = line + 1 

# 짝수번째 대각선이면, 분모는 커지고 분자는 작아지고
# 이걸로 뭐 해보고 싶었으나 어떻게 하는지 몰라서 실패함 ㅠ
if line % 2 == 0:

    ...