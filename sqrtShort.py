guess = number = float(input("Enter Number"))
while(round(guess**2,4) != round(number,4)):guess = (guess + (number / guess)) / 2
print("Estimate:",round(guess,15), "\nActual:\t ", number**.5)