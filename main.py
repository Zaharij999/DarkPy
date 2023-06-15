from random import *
user = input("Choose item: ")
list = ['камінь', "ножиці", "папір"]
comp = choice(list)
print(comp)
if comp == "камінь" and user == "камінь":
    print("Draw")
if comp == "камінь" and user == "ножиці":
    print("You lose")
if comp == "камінь" and user == "папір":
    print("You win")
if comp == "ножиці" and user == "камінь":
    print("You win")
if comp == "ножиці" and user == "ножиці":
    print("Draw")
if comp == "ножиці" and user == "папір":
    print("You lose")
if comp == "папір" and user == "камінь":
    print("You lose")
if comp == "папір" and user == "ножиці":
    print("You win")
if comp == "папір" and user == "папір":
    print("Draw")