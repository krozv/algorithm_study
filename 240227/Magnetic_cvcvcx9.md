# Magnetic
## 접근방법
- 위에서부터 아래로 아래에서부터 위로 
  같은 극을 만날 때까지 다른 극을 0으로 바꾼다.
- 그 뒤, 남은 자석들을 스택을 써서 교착상태를 체크할 수 있도록 만든다.
- 이때, 괄호체크와 같이 해버리면 안됨. 
  1 2 2 1 2 와 같이 나오는 경우, 스택에 2가 남아서, 1이 한번 더 교착상태로 체크됨
  
- 그래서 스택을 이용해 중복되는 극을 하나로 합치고, 스택에 남아있는 자석의 개수를 나눠 카운트했다.


