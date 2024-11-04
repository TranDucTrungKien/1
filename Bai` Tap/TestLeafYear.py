from LeafYear import checkleapyear, strtobool
while True:
    year=int(input("Input year:"))
    result=checkleapyear(year)
    if result==True:
        print(year,"is a leap year")
    else:
        print(year,"is NOT a leap year")
    ask=input("Continue?(y/n):")
    r=strtobool(ask)
    if r==False:
        print("Cut cmm di")
        break