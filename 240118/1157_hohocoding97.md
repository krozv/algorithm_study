## swea 1157 단어공부

#### 최근에 풀었던 방법
40040KB, 428ms
```python
word = list(input().strip().upper()) #입력받은 문자열을 대문자로 변경후 리스트로 변환
alphabet = list(set(word)) #word에 있는 알파벳을 하나씩만 담은 리스트
count_alphabet=[]

for i in alphabet:
    count_alphabet.append(word.count(i)) #count_alphabet이라는 리스트에 각 알파벳이 등장한 횟수를 추가

max_repeated_count = max(count_alphabet) #가장 많이 반복된 카운트 횟수
if count_alphabet.count(max_repeated_count) == 1: #가장 많이 사용된 알파벳이 하나만 존재할때
    position = count_alphabet.index(max_repeated_count)#count_alphabet에서 가장 많이 반복된 횟수의 위치찾기
    print(alphabet[position])
else:   #가장 많이 사용된 알파벳이 여러개 존재할때
    print('?')
```


#### 초기에 풀었던 방법(아스키코드)
33076KB, 68ms
```python
al = input().upper()
AtoZ = list(map(chr, range(65,91))) #A부터Z까지의 리스트 생성
num_of_al = []                    
for i in AtoZ:                      
    num_of_al.append(al.count(i))   #각 알파벳 개수 카운트
if num_of_al.count(max(num_of_al)) == 1:
    MaxAl = max(num_of_al)
    print(chr(num_of_al.index(MaxAl)+65)) 
    #num_of_al에서 'A'에 해당하는 위치는0이고 'A'의 아스키코드는 65이므로
else:
    print('?')
```