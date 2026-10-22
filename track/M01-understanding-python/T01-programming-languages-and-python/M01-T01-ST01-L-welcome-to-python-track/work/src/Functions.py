#add 2 nums
def add():
    a = 10
    b = 20
    print(a +b)

add()

#square
def square():
    a = 5
    print(a * a)

square()

#find the largest num in the list
def largest():
    a = 10
    b = 20
    c = 30
    if a>b and a>c:
        print(a)
    elif b>a and b>c:
        print(b)
    else:
        print(c)

largest()

#even or odd
def even_or_odd():
    a = 10
    if a % 2 == 0:
        print("Even")
    else:
        print("Odd")

even_or_odd()


#Greet with name
def greet():
    name = "Mahii"
    print("Helllloooo",name)

greet()



#TYPES OF FUNCTIONS

#type 1 - no input no output
def square():
    n=5
    print(n*n)

square()


#type 2 - no input , output

def square():
    n=5*5
    return n

print(square())

#type 3 input , no output

def square(n):
    res = n*n
    print(res)

square(3)


# type 4 - input , output

def square(n):
    return n*n
res = square(1)
print(res)


#type 1 - no input no output
def even_or_odd():
    n=5
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

even_or_odd()


#type 2 - no input , output

def even_or_odd():
    n = 5
    if n % 2 == 0:
        return "even"
    else:
        return "Odd"

print(even_or_odd())

#type 3 input , no output

def even_or_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

even_or_odd(3)


# type 4 - input , output

def even_or_odd(n):
    if n % 2 == 0:
        return "even"
    else:
        return "Odd"
res = even_or_odd(625)
print(res)