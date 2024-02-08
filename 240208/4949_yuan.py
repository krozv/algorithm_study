

dic = {')':'(', ']':'['}

#input 끝날때까지 돌아감
while True:
    a = input()
    st = []
    ans = ''

    if a == '.':
        break  # . 나올때마다 받아야함, 받아서 break

    # .까지의 받은 한줄에 대해서 판단
    for i in a:
        if i in '([':
            st.append(i)

        elif i in')]':
            if st:
                if st.pop() != dic[i]:
                    ans += 'no'
                    break
            else:
                ans += 'no'
                break

        else:
            continue

    if ans != 'no':
        print('yes')
    else:
        print(ans)
