#write four different python functions that calculates sine, cosine, additiion and subtraction. Also write a main function that calls these functions and prints the results

import math

def sine(x):
    return math.sin(x)

def cosine(x):
    return math.cos(x)

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def main():
    print("Sine of 30 degrees:", sine(math.radians(30)))
    print("Cosine of 45 degrees:", cosine(math.radians(45)))
    print("Addition of 5 and 3:", addition(5, 3))
    print("Subtraction of 10 and 4:", subtraction(10, 4))

if __name__ == "__main__":
    main()
