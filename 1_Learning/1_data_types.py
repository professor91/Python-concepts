# \n - next line
print("Bye World\n")

# data types
a = 2
print(a)
print(type(a))      # int

print("")

b = 2.0
print(b)
print(type(b))      # float

print("")

c = 'a'
print(c)
print(type(c))      # char

print("")

d = "String"
print(d)
print(type(d))      # string - is like a list (array)

print("")

t = True
f = False
print(t, f)
print(type(t), type(f))     # bool

print("")

# immutable & mutable

# tuple
# observe end
t = (1, "string", 2)
print(t)
for i in t:
    print(i, end= " ")
print("")
print(type(t))

print("")

# list
l = [1,2,3]
print(l)
for i in l:
    print(i, end= " ")
print("")
print(type(f))

# set
s= {12, "Hello", 45.6, True}
for i in s:
    print(i, end=" ")
print("")
print(type(t))