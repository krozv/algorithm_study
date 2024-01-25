> try_1
```py
N = int(input())

my_int = 2

while N >= my_int:
    if N % my_int == 0:
        N = N // my_int
        print(my_int)
        continue
    elif N == my_int:
        print(N)
    else :
        my_int +=1
        continue
```

<br><br>

> try_2   

```py
def Factoriziation():
    N = int(input())

    my_int = 2 #최소 인수 

    while N >= my_int:
        if N % my_int == 0: #나누어 떨어질 때
            N = N // my_int
            print(my_int)
            continue
        elif N == my_int: # 인수와 동일할 때 
            print(N)
        else :
            my_int +=1 #더이상 나누어 지지 않을 때
            continue
    
Factoriziation()
```
