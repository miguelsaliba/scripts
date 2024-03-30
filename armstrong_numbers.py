num = int (input("Please input the max number: "))
for j in range (1, num + 1):
  totl=0
  for i in range (len (str (j))):
    totl += int(str(j) [i]) ** len (str (j))
  if int (j) == totl:
    print (str (j) + " is an Armstrong number")