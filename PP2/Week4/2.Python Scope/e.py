n = 150
def myfunc():
    global n
    n = 200
myfunc()
print(n)