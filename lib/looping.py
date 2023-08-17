#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    for i in range(10,0,-1):
        print(i)
    print("Happy New Year!")

happy_new_year()

def square_integers(int_list):
    # code goes here!
    return [item**2 for item in int_list]
    

    pass
def fizzbuzz():
    # code goes here!
    for num in range(1,101):

        if num % 3==0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
         print("Fizz")
        elif num % 5 == 0:
            print ("Buzz")
        else:print(num)
fizzbuzz()
    
