#UCPC
full = input()
try:
    split_U = full.split('U',1)
except:
    print('I hate UCPC')
    exit()

try:
    split_U_C = split_U[1].split('C',1)
except:
    print('I hate UCPC')
    exit()

try:
    split_U_C_P = split_U_C[1].split('P',1)
except:
    print('I hate UCPC')
    exit()

try:
    if 'C' in split_U_C_P[1]:
        print('I love UCPC')
    else:
        print('I hate UCPC')
except:
    print('I hate UCPC')