def my_func(k):
  if(k > 0):
    result = k + my_func(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
my_func(6)