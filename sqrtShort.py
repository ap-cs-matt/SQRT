inputPrompt, number = "Please Enter A Number ", "Enter Number"
while(not number.isdigit()):  number, inputPrompt = input(inputPrompt), "Invalid Input - Please only enter a positive number"
number = guess = float(number)
while(round(guess**2,4) != round(number,4)): guess = (guess + (number / guess)) / 2
print("Estimate:",round(guess,4), "\nActual:\t ", number**.5)