# tech201_functions
tech201_functions

# Functions

 What is D R Y?
DRY stand for Don't repeat yourself it means you should keep the code short and simple

# What is a Functions?
A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

# Creating a function

```
def print_something():
print("Something has been printed")
print_something()
```

When you run this code it should Return "something has been printed"

# Functions and arguments

```def print_something(print_string):
print(print_string)
print_something("this is my variable")
print_something("This is the second time i called this function")
```
When you run this code it should Return "This is my variable"

"This is the second time i called this function"


# In Java:
 
```public void print_string(string_text)
def greeings(name):
    print("Hello my name is " + name)
greeings("Zain")
greeings("Skitz")
```

# The Return statement
```def addition(int1, int2):
    return int1 + int2
print(addition(2, 2))
```

Return 4
 
# Default arguments

 ```def addition(int1=2, int2=2):
return int1 + int2
print(addition())
print(addition(10, 10))
print(addition())
```

# Multiple arguments

```def multi_args(*multiargs):
    print(type(multiargs))

    for arg in multiargs:
        print(arg)

multi_args(1, 2, 3, 4, 5, 6)
```
 Type Hints



 def division(num1: int = 5, num2: int = 2) -> float:
    return num1 / num2

 print(division())

# Functions best practices

- name your functions clearly using lower case and underscores
-  All arguments should be clear in their need and where possible include in their expected type
- remember the return statement or your fuctions will return none
- keep functions small to preserve readability abd simplicity
- use comments in your functions to give instructions on how to use them
- consider using type hints to avoid type errors when you run your code

# Calculations

About the Program
- Created a calculator program which asks the user for two numbers and an operator
- The program checks to see if these inputs are valid
- Then based on the input the program completes the operation and outputs the answer
- I tried to implement and while loop to keep the calculator going but currently not functioning properly




