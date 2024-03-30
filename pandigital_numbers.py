x=str (int (input ("Please enter a number: ")))
z = [0,0,0,0,0,0,0,0,0,0]
ispan = True
for i in range (len (x)):
  z [int (x [i])] +=1
for i in range (10):
  if z [i] == 0:
    ispan = False
  else:
    print (str (i) + " is in "+ str (x) + " "+ str (z [i]) + " times.")
if ispan == True: 
  print (str (x) + " is a pandigital number.")
else:
  print (str (x) + " is not a pandigital number.")