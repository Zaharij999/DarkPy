from random import *
score1 = 0
score2 = 0
while True:
    user = input("Choose item: ")
    list = ['камінь', "ножиці", "папір"]
    comp = choice(list)
    print(comp)
    if comp == "камінь" and user == "камінь":
        print("Draw")
    if comp == "камінь" and user == "ножиці":
        print("You lose")
        score2 += 1
    if comp == "камінь" and user == "папір":
        print("You win")
        score1 += 1
    if comp == "ножиці" and user == "камінь":
        print("You win")
        score1 += 1
    if comp == "ножиці" and user == "ножиці":
        print("Draw")
    if comp == "ножиці" and user == "папір":
        print("You lose")
        score2 += 1
    if comp == "папір" and user == "камінь":
        print("You lose")
        score2 += 1
    if comp == "папір" and user == "ножиці":
        print("You win")
        score1 += 1
    if comp == "папір" and user == "папір":
        print("Draw")
    answer = input("Do you want to continue?")
    if answer == "yes":
        print("Your score:", score1, "Computer score:", score2)
    if answer == "no":
        break
    if score1 == 3:
        print("You win")
    if score2 == 3:
        print("You lose")