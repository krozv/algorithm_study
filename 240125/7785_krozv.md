# 7785. 회사에 있는 사람

## Solution

dictionary를 활용

key = name, value = state

key가 존재할 경우(=출퇴근 log가 있는 경우)를 조건으로 for문 만듦

```python
import sys

n = int(sys.stdin.readline())
log = {}
for _ in range(n):
    k, v = sys.stdin.readline().split()
    # log에 key가 존재하지 않을 경우, 새로운 키 생성
    if not log.get(k):
        log[k] = v
    # log에 key가 존재할 경우, dictionary update
    else:
        modify_log = {k: v}
        log.update(modify_log)

enter_person = []
for key in log.keys():
    # value가 enter인 경우만 enter_person list에 append
    if log[key] == 'enter':
        enter_person.append(key)
enter_person.sort(reverse=True)

for person in enter_person:
    print(person)

```