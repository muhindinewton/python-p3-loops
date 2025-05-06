#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while (i >=1 and i<=10):
        print(i)
        i -=1
    if i == 0:
        print ("Happy New Year!")

def square_integers(int_list):
    squared = []
    for num in int_list:
        squared.append(num ** 2)
    return squared
    pass

def fizzbuzz():
    for i in range (1,101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print (i)
    # code goes here!
    pass
