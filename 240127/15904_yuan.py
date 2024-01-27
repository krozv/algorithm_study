import sys

N = sys.stdin.readline()
N = list(N)


count = 0
for alpha in ['U','C','P','C']:    
    try: 
        index = N.index(alpha)
        N = N[index+1:]     
    except:
        count +=1
if count!= 0:
    print('I hate UCPC')
else:
    print('I love UCPC')