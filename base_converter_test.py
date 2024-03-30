arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = str (input ("Please input a number: "))
inBase = int (input ("Please input the base of the above number: "))
outBase = int (input ("Please input the base of the new number: "))
num = list (num.upper ())
origNum=str.join ('',num)
new_num=[]
tot=0
for i in range (len (num)):
  num [i] = arr.index (num [i])
for i in range(1,len (num)+1):
  tot+=int (num[len (num)-i])* (inBase**(i-1))
while tot!=0:
  new_num.insert (0,arr [tot%outBase])
  tot=tot//outBase
print ("\n"+origNum+" of base " +str (inBase)+ " in base "+str(outBase)+" is "+str.join ('',new_num))