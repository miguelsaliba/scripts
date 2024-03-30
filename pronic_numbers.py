num = int (input("Please input a number: "))
x = int (num**(.5)) #int of Square root of num
if x*(x+1) == num:
  print (str (num) + " is a pronic number.")
else:
  print (str (num) + " is not a pronic number.")