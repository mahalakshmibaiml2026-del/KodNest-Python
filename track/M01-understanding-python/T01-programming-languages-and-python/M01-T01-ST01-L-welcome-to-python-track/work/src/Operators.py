# Arithematic operators

print(3 + 3)
print(3 - 3)
print(3 * 3)
print(3 / 3)
print(3 // 3)
print(3 % 3)
print(3 ** 3)

print(1 / 3)
print(100 % 3)
print(13 / 3)

# Comparasion operators (True\False)

print(11 == 11)
print(11 != 10)
print(11 > 10)
print(11 < 10)
print(11 >= 10)
print(11 <= 10)

# Assignment operators

a = 10
print(a)
a += 10
print(a)
a -= 10
print(a)
a *= 10
print(a)
a /= 10
print(a)
a %= 10
print(a)
a **= 10
print(a)
a //= 10
print(a)


# Logical operators

a = True
b = False
#AND both should be true
#OR any one should be true
print(a and b)
print(a or b)
print(not a)
print(not b)
a = (5 > 3) and (4 < 6) 
a = (5 > 3) or (4 < 6)
a = not (5 > 3) 

#Identity operators

a = 10
b = 10
print(a is b) 
print(a is not b)

#Membership operators

a = 10
b = [1,4,2,65] 
print(a in b) #F
print(1 in b) #True
print(a not in b) #True

# Bitwise operator

a = 2
b = 3
print(a & b) #2
print(a | b) #3
print(a ^ b) #1

a = 5
print(a << b) #40
print(a >> b) #0