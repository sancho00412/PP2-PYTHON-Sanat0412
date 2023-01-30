a = int(input())
b = int(input())
c = int(input())
print(a + b + c)
print(a - b - c)
print(a * b * c)
print((a / b)/c)
if a > b and b > a:
    print("maximum is a")
else:
    print("Not a at the maximum")
if a > b or b > c:
    print("nice")
else:
    print("bad")
if a == b & a != c:
    print("yes")
if a <= b | a <= c:
    b += a
    print(b)
print(a%b,a%c)
print(a**b)
print(a/b,a//b)