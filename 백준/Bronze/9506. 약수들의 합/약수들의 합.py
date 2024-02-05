import sys
while True:
  n = int(sys.stdin.readline())
  if n == -1:
    break
  list = []
  for i in range(1,n):
    if n%i == 0:
      list.append(i)
  if sum(list) == n:
      print(str(n), '=', ' + '.join(map(str,list)))
  else:
      print(str(n), "is NOT perfect.")