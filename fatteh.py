x = [0, 7, 5, 3]
while True:
  print("1) " + "0" * x[1] + "X" * (7-x[1]))
  print("2) " + "0" * x[2] + "X" * (5-x[2]))
  print("3) " + "0" * x[3] + "X" * (3-x[3]))
  while True:
    row = input("Enter row: ")
    if row not in [1, 2, 3]:
      continue
    amount = input("Enter amount: ")
    if amount > x[row] or amount < 1:
      continue
    x[row] = x[row] - amount
    if x == [0, 0, 0, 0]:
      x = [0, 7, 5, 3]
    break
