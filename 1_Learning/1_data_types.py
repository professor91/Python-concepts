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

# observe end
e = (1, "string", 2)
print(e)
for i in e:
    print(e, end= "-")
print("")
print(type(e))      # tuple

print("")

f = [1,2,3]
print(f)
for i in f:
    print(i, end= "-")
print("")
print(type(f))      # list