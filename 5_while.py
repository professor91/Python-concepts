# cannot declare i directly in while as done in for loops
i= 0

# while loop
while i < 10:
   print(i, end = " ")
   i += 1

print("\n**********************************************************")

# else in while loop 
j = 0
while j < 10:
   print(j, end = " ")
   j += 1
else:
   print("\nj has reached 10 now.")

print("**********************************************************")

# Python do not have do-while loop