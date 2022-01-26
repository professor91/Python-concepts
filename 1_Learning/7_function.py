# functions are like modules used to perform a repetative tasks again and again

# function defined - without parameters
def func1():
    print("I am in function 1.")
    print("**********************************************************")
    

# function defined - with parameters
def func2(x : int, y: str):
    print("I am in function 2.")
    print("Value of x is: " + str(x))
    print("Value of x is: " + y)
    print("**********************************************************")

# function defined - with default parameters
def func3(x = 3):
    print("I am in function 3.")
    print("Value of x is: " + str(x))
    print("**********************************************************")

# function defined - with variable parameters (as tuples)
def func4(*args):
    print("I am in function 4.")
    for i in args:
        print(i, end= "-")
    print("\n**********************************************************")

# function defined - with variable parameters (as dictionary)
def func5(**kwargs):
    print("I am in function 5")
    for i in kwargs.keys():
        print(i + " : " + str(kwargs[i]))
    print("**********************************************************")

# function defined - returning a value
def func6(x, y):
    return x + y

# calling functions
func1()

func2(x= 1, y= "hello")

func3()
func3(5)

func4(1,2,3,4)

func5(a= 1, b= 2, c= 3)

print("Sum is: " + str(func6(2,2)))






# number_of_students= int(input("Enter the number of students: "))

# # functions defined
# def get_data():
#     name = input("Enter the name of the student: ")
#     age= int(input("Enter the age of the student: "))
#     rollno= int(input("Enter the roll number: "))

#     print("Name of the student: " + name)
#     print("Age of the student: " + str(age))
#     print("Roll number: " + str(rollno))

#     print("**********************************************************\n")


# for i in range(number_of_students):
#     # function called
#     get_data()