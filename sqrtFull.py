validInput = False
while(not validInput):
    number = input("Enter Number")  # sets the initial guees and the number that you are finding the sqrt of to the input
    try:
        number = guess = float(number)
        break
    except:
        print("Error")

while(round(guess**2,4) != round(number,4)): #stops the loop if the approximation is equal to within 4 decimal places
    underEstimate = number / guess
    guess = (guess + underEstimate) / 2 #sets guess to the average of the distance betweent he current guess (an oversetimate) and the number divided by the current guess (an undersetimate)

print("Estimate:",round(guess,4)) #prints the estimate
print("Actual:\t ", number**.5) #prints the actual value