# Way 1
math = float(input("Math Score: "))
physics = float(input("Physics Score: "))
chemistry = float(input("Chemistry Score: "))
avg = (math + physics + chemistry) / 3
print("Average score =", avg)
print("Average score (rounded) =", round(avg, 2))


# Way 2
print("GPA Calculator")
math, physics, chemistry = eval(input("Enter math, physics, chemistry scores (comma separated): "))
print("Math Score =", math)
print("Physics Score =", physics)
print("Chemistry Score =", chemistry)
avg = (math + physics + chemistry) / 3
print("Average score =", avg)
print("Average score (rounded) =", round(avg, 2))