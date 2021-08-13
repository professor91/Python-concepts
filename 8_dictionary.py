# dictionary consists of a key and values associated to that key

dicti= {
            "a" : [1],
            "b" : [2],
            "c" : [3],
            "d" : [4],
            "e" : [5],
            "f" : [6]
}
print(dicti)
print("**********************************************************")

# adding more values to a key
dicti["c"].append(6)
dicti["d"].append(7)

# getting keys of the dictionary in a list
keylist = dicti.keys()
print("Keys: ", end= " ")
for keys in keylist:
    print(keys, end= " ")

print("\n**********************************************************")

# getting value of a key
print("Values: ", end= " ")
valuelist= dicti.values()
for values in valuelist:
    print(values, end= " ")

print("\n**********************************************************")

