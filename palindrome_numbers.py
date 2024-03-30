x = str (input ("Please enter a number: "))
i = len (x) - 1
z = ""
while i >= 0:
  z+=str(x [i])
  i-=1
if z == x:
  print (x + " is a palindrome number.")
else:
  print (x + " is not a palindrome number.")