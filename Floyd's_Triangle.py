num = int(input())
currentNum = 1
for i in range(num+1):
  output = ""
  for j in range(i):
    output += (str(currentNum)+ " ")
    currentNum += 1
  print (output)