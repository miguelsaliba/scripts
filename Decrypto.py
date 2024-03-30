arr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
x = list (input().upper())
a = []
for i in range(len(x)):
  if x [i] not in arr:
    a.append(x [i])
  else:
    b = 25 - arr.index (x[i])
    a.append (arr [b])
print (''.join(a))