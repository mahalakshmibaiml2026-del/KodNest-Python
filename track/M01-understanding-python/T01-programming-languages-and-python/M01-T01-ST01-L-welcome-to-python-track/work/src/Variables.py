name = "Maha"
age = 23
print(name)
print(id(name))
print(type(name))

print("Hello Python")
print("thank you python")

print("Hello Python", end=" ")
print("thank you python")

print("Hello Python", end=" - ")
print("thank you python")

print("Hello Python \n thank you python")

print("Hello Python \nthank you python")

print("my name is " ,name,"and my age is",age)
print("my name is " + name + "and my age is" + str(age))

#formatting strings 
print(f"My name is {name} and age is {age}")

#single - line comments

""" Multi - line comments
Hello
Hi
Thank You
"""

a = 10
b = 20
c = 30

#a,b,c=10,20,30
# = b = c = 10

print(a+b+c)

a,b,c="Abhi","balu","cinu"
print(a+b+c)

x,y,z=30,6,2
print(x+y+z)
#print(a+x) will not work bcuz they are different data types
print(a+str(x))
print(a,x)
print(b+c)

a=27
print(type(a),a)