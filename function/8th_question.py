# Q8. Function with **kwargs
# Problem: Create a function that accepts any number of keyword arguments
# and prints them in the format key: value.


def print_kwarg(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
    
print_kwarg(name="sanu", power="laser")    