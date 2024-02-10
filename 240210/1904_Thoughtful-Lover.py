'''
1904. 01 타일

00 타일과 1 타일 2가지
N이 주어졌을 때,
위의 두 가지 타일로 N개를 덮는 경우의 수

첫 번째 줄에 지원이가 만들 수 있는 길이가 N인 모든 2진 수열의 개수를 15746으로 나눈 나머지를 출력한다.
'''


def tile(num):      # 타일의 개수가 피보나치 수열임을 파악
    minus_1 = 1
    minus_2 = 0
    sum = 0

    for i in range(num):
        sum = minus_1 + minus_2
        minus_2 = minus_1
        minus_1 = sum

    return sum%15746


N = int(input())
print(tile(N))