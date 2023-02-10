class Person:
  def __init__(object, name, age):
    object.name = name
    object.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("Alua", 18)
p1.myfunc()