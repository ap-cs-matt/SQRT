number = ""
while(not number.isdigit()):
    guess = number = input("Enter Number")
number = guess = float(number)
while(round(guess**2,4) != round(number,4)): #stops the loop if the approximation is equal to within 4 decimal places
    underEstimate = number / guess
    guess = (guess + underEstimate) / 2 #sets guess to the average of the distance betweent he current guess (an oversetimate) and the number divided by the current guess (an undersetimate)

print("Estimate:",round(guess,4), "Actual:\t ", number**.5) #prints the estimate