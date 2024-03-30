from math import sqrt

 
def reduced_sqrt(n):
  """Return most reduced form of square root of n as the couple (coefficient, reduced_form) """
  root = int(sqrt(n))
  
  for factor_root in range(root, 1, -1):
    factor = factor_root * factor_root
    if n % factor == 0:
      reduced = n // factor
      return (factor_root, reduced)
      
  return (1, n)

  
def print_reduced_sqrt(n):
  coefficient, reduced = reduced_sqrt(n)
  if coefficient == 1:
    print('\u221A', reduced)
  
  elif reduced == 1:
    print(coefficient)
 
  else:
    print(coefficient, '\u221A', reduced)

