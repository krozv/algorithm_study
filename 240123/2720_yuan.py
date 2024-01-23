
T = int(input())


for _ in range(T):
    C1 = int(input())

    p = 25
    q = 10
    r = 5
    s = 1

    numb1 = 0
    while C1 > numb1 * p :
        numb1 += 1
    else:
        if C1 != numb1 * p:
            numb1 -= 1
        else:
            pass


    C2 = C1 - numb1 * p
    numb2 = 0
    while C2 > numb2 * q : # 19> 10
        numb2 += 1
    else:
        if C2 != numb2 * p:
            numb2 -= 1
        else:
            pass


    C3 = C2 - numb2 * q   # 19 - 10 = 9
    numb3 = 0
    while C3 > numb3 * r: # 9 > 5
        numb3 += 1
    else:
        if C3 != numb3 * p:
            numb3 -= 1
        else:
            pass


    C4 = C3 - numb3 * r
    numb4 = 0
    while C4 != numb4 * s:
        numb4 += 1


    print(f'{numb1} {numb2} {numb3} {numb4}')