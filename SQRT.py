from math import *
k = guess = number = float(input("Enter Number"))
while(guess**2 != number and k < number + 100):
    guess, k  =  (guess + (number / guess)) / 2, k + 1
print("Estimate:",guess, "\nActual:\t ", sqrt(number))