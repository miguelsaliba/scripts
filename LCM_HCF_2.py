x = 0
num=[[1]]
maxi=0
while len(num) == 1:
  num = [[int(f)] for f in input("Please input 2 or more numbers separated by commas: ").split(",")]
i = len(num)
q=num [0][0]
for j in range (i):
  if num[j][0] > maxi:
    maxi = num[j][0]
  for x in range (1,int (num[j][0]/2+1)):
    num [j].append (x)
  for b in range(2, len (num [j])+1):
    if b in num [j]:
      if num [j][0] % b != 0:
        num [j].remove(b)
l = num [0]
for d in range (i):
  c=0
  while True:
    if not l[c] in num [d]:
      del l[c] 
    else:
      c+=1
    if c> len (l)-1:
      break
print ("\nHCF is " + str (max (l))+ "\n")
num[0].insert(0,q)
for e in range (1, 100000):
  if all ((maxi * e) % num[n][0] == 0 for n in range (i)):      
    print ("LCM is " + str(maxi * e))
    break
