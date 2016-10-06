g=n=float(input("Enter Number"))
while(round(g**2,4)!=round(n,4)):g=(g+(n/g))/2
print("Estimate:",round(g,4),"\nActual:\t ",n**.5)