num = int (input ("Please enter a number: "))
l = []
for i in range(1,int (num/2)):
  if i not in l:
    if num%i == 0:
      l.append (i)
      if num/i not in l:
        l.append (int (num/i))
print("\nThe factors of "+str (num)+" are "+str (l))
sum = 0
for j in range(len (l)-1):
  sum+=l [j]
print ("\nThe sum of all the factors is " + str (sum))
print ("\n"+str(num)+" times 2 is "+str (num*2))
if int (num*2)<sum:
  print("\n"+str (num)+" is an abundant number.")
else:
  print ("\n"+str (num)+" is not an abundant number.")