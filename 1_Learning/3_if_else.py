choice = int(input("Enter your choice: "))

print("**********************************************************")

# if-else
if choice == 1:
    print("You choose 1.")
else:
    print("You did not choose 1.")

print("**********************************************************")

# nested if-else
if choice == 1:
    print("You choose 1.")
elif choice == 2:
    print("You choose 2.")
elif choice == 3:
    print("You choose 3.")
elif choice == 4:
    print("You choose 4.")
else:
    print("You did not choose either of 1,2,3,4.")