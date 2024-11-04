while True:
    x=int(input('Enter a numer: '))
    print(x,' is an even number.' if x%2==0 else ' is an odd number.')
    ques=input('Continue? (Yes/No): ')
    if ques=='No':
        break
print('Bye! Thank you')