# ! syntax
"""
def functionname( parameters ):
   "function_docstring"
   function_suite
   return [expression]
"""


# Function definition is here
def myprint(str):
    """This prints a passed string into this function"""
    print(str)
    return


# Now you can call printme function
myprint("I'm first call to user defined function!")
myprint("Again second call to the same function")

# ! Pass by reference vs value
# Function definition is here
def changeme(mylist):
    """This changes a passed list into this function"""
    mylist.append([1, 2, 3, 4])
    # mylist = [1, 2, 3, 4];  # This would assign new reference in mylist
    print("Values inside the function: ", mylist)
    return


# Now you can call change me function
# mylist = [10, 20, 30]
# changeme(mylist)
# print("Values outside the function: ", mylist)


# !! Function Arguments
# # ? Required arguments
def printme(str):
    """This prints a passed string into this function"""
    print(str)
    return


# printme()  # TypeError: printme() missing 1 required positional argument: 'str'


# # ? Keyword arguments
# Function definition is here
def printinfo(name, age):
    """This prints a passed info into this function"""
    print("Name: ", name)
    print("Age ", age)
    return


# printinfo(age=50, name="miki")


# # ? Default arguments
def printinfo(name, age=35):
    """This prints a passed info into this function"""
    print("Name: ", name)
    print("Age ", age)
    return


# printinfo(age=50, name="miki")
# printinfo(name="miki")

# # ? Variable-length arguments
'''
def functionname([formal_args,] *var_args_tuple ):
   "function_docstring"
   function_suite
   return [expression]
'''


def printinfo(arg1, *vartuple):
    """This prints a variable passed arguments"""
    print("Output is: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return


# printinfo(10)
# printinfo(70, 60, 50)


# ! The return Statement
def sum(arg1, arg2):
    # Add both the parameters and return them."
    total = arg1 + arg2
    print("Inside the function : ", total)
    return total


total = sum(10, 20)
# print("Outside the function : ", total)

# ! Global vs. Local variables
new_total = 0  # This is global variable.


def sum(arg1, arg2):
    # Add both the parameters and return them."
    new_total = arg1 + arg2;  # Here total is local variable.
    print("Inside the function local total : ", new_total)
    return total


sum(10, 20);
print("Outside the function global total : ", new_total)
