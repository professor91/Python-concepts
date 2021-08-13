#using break the program exits the main loop (in this case for loop)

for number in range(1, 21) :
    if( number == 12) :
        break
    print(number, end = " ")

print("\n**********************************************************")

#using continue the progeam exits only the loop in which it is present (in this case it is if.2)

for number in range(1, 21) :
    if( number == 12) :
        continue
    print(number, end = " ")

print("\n**********************************************************")