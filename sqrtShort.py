k = guess = number = float(input("Enter Number"))
while(k < number + 1000 and round(guess**2,4) != round(number,4)):guess, k = (guess + (number / guess)) / 2, k + 1
print("Estimate:",round(guess,4), "\nActual:\t ", number**.5)