from GPAib import calcGPA
qt=float(input("Input on-going:"))
gk=float(input("Input mid term:"))
ck=float(input("Input final:"))
avg=calcGPA(qt,gk,ck)
print(f'GPA={avg}')
