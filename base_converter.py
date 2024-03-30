num = int(input("Please enter a number: "))
base = int(input("Please enter a base: "))
x=num
new_num = []
arr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while x != 0:
  if x%base < 10:
    new_num.insert (0,str (x%base))
  else:
    new_num.insert (0,arr [(x%base)-10])
  x = x//base
x=""
print (str.join('',new_num))