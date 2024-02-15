'''
첫째줄 : N
둘째줄 : N 개의 수로 이루어진 수열
셋째줄 : (+의 개수) (-의 개수) (*의 개수) (//의 개수)

숫자들 사이사이에 임의의 연산자를 넣어 연산을 할 때
최대값과 최소값을 출력

힌트를 봤을 때 연산은 앞에서부터 순서대로 수행한다.
'''

'''
순열 문제네!
미안 근데 일단 막 풀고 순열공부 다시해야겠어,, 하하
막 풀리지도 않아
'''

'''
예제 입력 1

3
5 6 4
1 0 1 0 / 2 0 0 0
'''


def f(i, k):
    global min_sum
    global max_sum

    if i == k:
        sum = arr[0]
        for j in range(k+1):
            if operator[j] == '+':
                sum = sum + arr[j+1]
            elif operator[j] == '-':
                sum = sum - arr[j+1]
            elif operator[j] == '*':
                sum = sum * arr[j+1]
            elif operator[j] == '//':
                sum = sum // arr[j+1]

        if min_sum > sum:
            min_sum = sum
        if max_sum < sum:
            max_sum = sum

    else:
        for l in range(i, k):
            operator[i], operator[l] = operator[l], operator[i]
            f(i+1, k)
            operator[i], operator[l] = operator[l], operator[i]


N = int(input())
arr = list(map(int, input().split()))
a, s, m ,p = map(int, input().split())
operator = [0]*a + [1]*s + [2]*m + [3]*p        # 0 = +, 1 = -, 2 = *, 3 = //
min_sum = 1000000000
max_sum = -1000000000

f(0, N-2)

print(max_sum)
print(min_sum)


'''
# 앞에 하던거 뭉갬
def operator_input(l1, l2):
    while len(l1) > 1:
        # 연산자가 결정되면
        l1[1] = l1[0] 연산자 l1[1]
        l1.pop(0)

def permutation(i, k):
    if i == k:
        for j in operator:
            if j == '+':
                l1[1] = l1[0] + l1[1]
                l1.pop(0)
            elif j == '-':
                l1[1] = l1[0] - l1[1]
                l1.pop(0)
            elif j == '*':
                l1[1] = l1[0] * l1[1]
                l1.pop(0)
            elif j == '//':
                l1[1] = l1[0] // l1[1]
                l1.pop(0)

    
    # operator[0] => +
    # operator[1] => -
    # operator[2] => *
    # operator[3] => //
    





N = int(input())
arr = list(map(int, input().split()))
operator = list(map(int, input().split()))

def(arr, operator)
'''