def myfunc(a):
  return lambda x : x * a

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(55))
print(mytripler(55))