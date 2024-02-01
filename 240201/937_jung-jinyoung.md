### try_1 (대실패)
```py
class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        dig = [log for log in logs if log[:3] == "dig"]
        let = [log for log in logs if log[:3] == "let"]
        # dig = list()
        # let = list()
        # for log in logs:
        #     if log[:3] == "dig":
        #         dig.append(log)
        #     else :
        #         let.append(log)

        let.sort()
        dig.sort()

        return let+dig

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6",
        "let2 own kit dig","let3 art zero"]
sol = Solution()
result = sol.reorderLogFiles(logs)
print(result)
```

결과   

>['let1 art can', <span style="color:pink">'let2 own kit dig', 'let3 art zero'</span>, 'dig1 8 1 5 1', 'dig2 3 6']

정답  
>["let1 art can",<span style="color:pink">"let3 art zero","let2 own kit dig"</span>,"dig1 8 1 5 1","dig2 3 6"]   

문제점  
- 정렬의 기준을 단순하게 가장 첫 문자를 기준으로 정함  
- digit 과 letter 이라는 문제의 기준을 읽고 다시 생각함   
- digit일 경우 입력 순서로 정렬  
- letter일 경우 : 식별자 첫 글자 -> 두번째부터의 문자열 정렬   

### try_2 (실패)
#### study
##### 정렬, 다중 조건

`sorted(list, key = lambda x: x[1])`   
key 인자에 함수를 넘겨주면 해당 함수의 반환값을 비교하여 내가 설정한 순서대로 정렬한다.   
<br>
`sorted(e, key = lambda x : (x[0], -x[1]))` 
아이템 첫 번째 인자를 기준으로 오름차순으로 먼저 정렬  
-> 두 번째 인자를 기준으로 내림차순 정렬 

---
<br>

```py
class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        let = list()
        dig = list()
        for log in logs:
            if log.split()[1].isdigit():
                dig.append(log) # 숫자 로그 : 입력된 순서대로 정렬
            else :
                let.append(log)
        # 문자 로그 정렬
        # 정렬 다중 조건 : lamda를 사용
        
        let = sorted(let, key = lambda let : let.split()[1:]) # 다음 문자열로 순서로 정렬 # 처음에 틀림
        #['a2 act car', 'g1 act car', 'a8 act zoo', 'ab1 off key dog']
        return let + dig
```
> 예시 문제는 정답이 맞았으나 반례가 있음  

#### 반례

`input:
logs =
["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]`   
<br>
`output:
["g1 act car","a2 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
`    
<br>
`expected:
["a2 act car","g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
`   

---
문제점 
- 첫번째 식별자를 정렬을 안하고 두번째 문자열부터의 정렬을 시도함  
- 정렬 순서 인식  
    1. 첫번째 문자 식별자 정렬
    2. 두번째부터의 문자열 정렬  

### try_3 (성공)

```py
class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        let = list()
        dig = list()
        for log in logs:
            if log.split()[1].isdigit():
                dig.append(log) # 숫자 로그 : 입력된 순서대로 정렬
            else :
                let.append(log)
        # 문자 로그 정렬
        # 정렬 다중 조건 : lamda를 사용
        let = sorted(let, key = lambda let : let.split()[0]) # 첫번째 문자로 정렬
        #['a2 act car', 'a8 act zoo', 'ab1 off key dog', 'g1 act car']
        let = sorted(let, key = lambda let : let.split()[1:]) # 다음 문자열로 순서로 정렬 # 처음에 틀림
        #['a2 act car', 'g1 act car', 'a8 act zoo', 'ab1 off key dog']
        return let + dig
```


