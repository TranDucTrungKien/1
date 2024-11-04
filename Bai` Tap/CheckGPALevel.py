def GPA(d):
    if 0<d<5: return 'bad'
    elif 5<=d<7: return 'pass'
    elif 7<=d<8.5: return 'strong pass'
    elif 8.5<=d<=10: return 'good'
    else: return 'Invalid'
name=str(input('Enter name:'))
d=float(input('Enter GPA:'))
print(name,GPA(d))