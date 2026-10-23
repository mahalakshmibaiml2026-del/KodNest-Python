def add(a,b):
    print(a+b)

def add(a,b,c):
    print(a+b+c)

def add(a,b,c,d):
    print(a+b+c+d)
#add(12,12) will be error and same goes with add(2,3,4)
add(10,34,22,34)

#default values
def add(a,b=0,c=0):
    print(a+b+c)

add(10,20)
add(10,33,23)
add(10)

# *args - 0...n arguments can be passed --> tuple

def add(*a):
    print(sum(a))

add(10,20)
add(10,33,23)
add(10)
add()


# **kwargs - 0...n arguments acn be passed --> dict

def stu_info(**kwargs):
    print(f"Name is {kwargs.get('name')}", end = "")
    print(f"Age is {kwargs.get('age')}", end = "")
    print(f"Course is {kwargs.get('course')}")

stu_info(name = "MAHII" , age = 23, course = "Python")