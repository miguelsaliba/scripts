i = 0
num = [[1]]
x = 0
maxi = 0
while num [i][0] != 0:
  i+=1
  num.append([int (input("Please input a number. (enter 0 to stop inputting numbers): "))])
  if num [len (num) -1][0] == 0 and i < 2:
    print ("Please enter one or more numbers.")
    del num[len (num) - 1]
    i-=1
  if num [i][0] > maxi:
    maxi = num [i][0]
del num [len (num)-1]
del num [0]
q=num [0][0]
for j in range (i-1):
  for x in range (1,int (num[j][0]/2+1)):
    num [j].append (x)
  for b in range(2, len (num [j])+1):
    if b in num [j]:
      if num [j][0] % b != 0:
        num [j].remove(b)
l = num [0]
for d in range ( i-1):
  c=0
  while True:
    if not l[c] in num [d]:
      del l[c] 
    else:
      c+=1    
    if c> len (l)-1:
      break
print ("\nHCF is " + str (max (l))+ "\n")
num [0].insert (0,q)
for e in range (1, 100000):
  if all ((maxi * e) % num[n][0] == 0 for n in range (i-1)):      
    print ("LCM is " + str(maxi * e))
    break