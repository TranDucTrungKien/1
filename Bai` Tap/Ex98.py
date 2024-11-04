from random import randrange

for i in iter(int,1):
    machine = randrange(1, 101)
    win = False
    for count in range(1, 8):
        human = int(input("Guessing Machine [1..100], please guess: "))
        print("Your times guessing: ", count)
        if machine == human:
            print("Congratulations you guessed correctly, machine number is", machine)
            win = True
            break
        if machine > human:
            print("Wrong, computer number > your number")
        elif machine < human:
            print("Wrong, computer number < your number")
    if win ==False:
        print("GAME OVER!, computer number =", machine)
    ask = input("Continue? ")
    if ask == "n":
        break
print("Khong choi nua thi Cut'")