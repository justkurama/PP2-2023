#Local scope
def myfunc():
  x = 300
  print(x)

myfunc()

#Function Inside Function
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()