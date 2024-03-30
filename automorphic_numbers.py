num = int (input ("Please enter a number: "))
for j in range (1, num):
  totl = ""
  sqr = j ** 2
  for i in range(len (str (sqr)) - len(str (j)), len (str (sqr))):
    totl += str (sqr)[i]
  if int(totl) == int(j):
    print (str(j) + " is an automorphic number")