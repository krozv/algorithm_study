x = int(input())
t = 1
sum = 0
while t<= x:
  lines = map(int, input().split())
  for i in list(lines):
    if i % 2 == 1:
      sum += i
 
  print("#"+str(t)+" "+str(sum))
  sum=0
  t += 1
