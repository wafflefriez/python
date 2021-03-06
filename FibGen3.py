# Importing modules
import time
import os

# Define initial delay time
delay = 0.25

# Defining functions
def new_line():
    print("\n")

def wait_and_clear():
    time.sleep(delay)
    clear = lambda: os.system('clear')
    clear()

def blood_magick(val1, val2):
    return val1 + val2

# Defining initial variables
x = float('inf')
a = 1
b = 1
c = 0

# Printing welcome
wait_and_clear()
new_line()
print("Welcome to the Fibonacci Number Generator v3.1!")
time.sleep(2)
new_line()
print("Created by: Eric Driggers")
print("Last Update: 10/23/2018")
time.sleep(2)
wait_and_clear()

new_line()
delay = input("First, set the delay: ")
delay = float(delay)
time.sleep(0.25)
wait_and_clear()

new_line()
print("Great. Let us begin!")
time.sleep(2)
wait_and_clear()

new_line()
print(str(a))
wait_and_clear()

new_line()
print(str(b))
wait_and_clear()

# While loop
while c < x:
    c = blood_magick(a, b)
    new_line()
    print(str(c))
    wait_and_clear()

    a = blood_magick(b, c)
    new_line()
    print(str(a))
    wait_and_clear()

    b = blood_magick(c, a)
    new_line()
    print(str(b))
    wait_and_clear()
