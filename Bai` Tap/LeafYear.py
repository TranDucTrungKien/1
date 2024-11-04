def checkleapyear(year):
    if(year%4==0 and year%100!=0) or year%400==0:
        return True
    return False
def strtobool(s):
    return s.lower() in ("y","c","yes","1")
