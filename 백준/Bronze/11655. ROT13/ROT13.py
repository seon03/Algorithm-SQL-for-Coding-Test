S = input()
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
b = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
for i in range(len(S)):
  if S[i] in a:
    print(b[a.index(S[i])], end="")
  else:
    print(S[i], end="")