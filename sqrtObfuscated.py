k=g=n=float(input("Enter Number"))
while(k<n+1000 and round(g**2,4)!=round(n,4)):g,k=(g+(n/g))/2,k+1
print("Estimate:",round(g,4),"\nActual:\t ",n**.5)