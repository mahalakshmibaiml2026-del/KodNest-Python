c = 30 #global variable
def add():
    global a
    a = 10 #local variable
    b = 20
    print(a+b)
    print(c)

add()


x = 100
def display():
    x = 50
    print("Local x:" ,x)
display()
print("Global x:",x)


x = 10
def display():
    print(x)
display()
x=30
print(x)