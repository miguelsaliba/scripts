from math import cos, tan, radians
import simplify_radicals

co = {30: [2,3], 45: [2,2], 60: [2]}
ta = {30: [3,3], 45: [1],   60: [1,3]}
circle = input("(ins/circum): ").lower()
while circle != 'ins' and circle != 'circum':
  circle = input('Error, please use "ins" or "circum": ').lower()
sides = int (input ("Number of sides: "))
while sides < 3:
  sides = input("How could u have less than 3 sides? Try to do it properly this time: ")
side = float (input ("Measure of one side: "))
halfAngle = (90 * (sides-2))/sides


if circle == 'ins':
  if halfAngle in ta:
    if len(ta[halfAngle]) == 2:
      print((side/2)/ta[halfAngle][0],'\u221A',ta[halfAngle][1])
    else:
      print((side/2)/ta[halfAngle][0])
  else:
    print_reduced_sqrt((side/2)*tan (radians (halfAngle)))

elif circle == 'circum':
  if halfAngle in co:
    if len(co [halfAngle]) == 2:
      print (((side/2) * co[halfAngle][0]) / co[halfAngle][1],'\u221A',co[halfAngle][1])
    else:
      print((side/2) * co[halfAngle][0])
  else:
    print_reduced_sqrt((side/2) / cos(radians (halfAngle)))

else:
  print("I don't know how you got here but good job.")