a = 2

for i in range(1, 11):
    # formatiing stringss
    print(f"{a} * {i} = {a*i}")

print("\n**********************************************************\n")

for i in range(1, 11):
    # formatiing stringss
    print("{0} * {1} = {2}".format(a, i, a*i))

print("\n**********************************************************\n")

word = 'Characterstics'

print(word)

for letter in word :
    print(letter, end = '-')