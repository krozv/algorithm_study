
def 소인수분해(N):
    for i in range(2, 10000000):
        k,v = divmod(N,i)
        if k>0 and v ==0:
            print(i)
            return 소인수분해(k)


N=int(input())

if N == 1:
    print()
else:
    소인수분해(N)
