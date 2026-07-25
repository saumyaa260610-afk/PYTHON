#SNAKE WATER GUN GAME
while True:
    import random
    comp=random.choice(["snake", "water","gun"])
    print("SNAKE, WATER,GUN GAME")
    player=input("enter choice, snake, water or gun?").lower()
    if comp=="snake":
        if player=="snake":
            print("Tie. The computer also chose snake.")
        elif player=="water":
            print("You lost.The computer chose snake.")
        elif player=="gun":
            print("You won! The computer chose snake.")
        else:
            print("invalid choice. try.again")
    elif comp=="water":
        if player=="snake":
            print("You won! The computer chose water.")
        elif player=="water":
            print("Tie. The computer also chose water.")
        elif player=="gun":
            print("You lost.The computer chose water.")
        else:
            print("invalid choice. try.again")
    else:
        if player=="snake":
            print("You lost.The computer chose gun.")
        elif player=="water":
            print("You won! The computer chose gun.")
        elif player=="gun":
            print("Tie. The computer also chose gun.")
        else:
            print("invalid choice. try.again")
    choice=input("would u like to continue?").lower()
    if choice=='no':
        break

#using functions
print("SNAKE, WATER,GUN GAME")
while True:
    def game():
        import random
        comp=random.choice(["snake", "water","gun"])
        player=input("enter choice, snake, water or gun?").lower()
        if comp=="snake":
            if player=="snake":
                print("Tie. The computer also chose snake.")
            elif player=="water":
                print("You lost.The computer chose snake.")
            elif player=="gun":
                print("You won! The computer chose snake.")
            else:
                print("invalid choice. try.again")
        elif comp=="water":
            if player=="snake":
                print("You won! The computer chose water.")
            elif player=="water":
                print("Tie. The computer also chose water.")
            elif player=="gun":
                print("You lost.The computer chose water.")
            else:
                print("invalid choice. try.again")
        else:
            if player=="snake":
                print("You lost.The computer chose gun.")
            elif player=="water":
                print("You won! The computer chose gun.")
            elif player=="gun":
                print("Tie. The computer also chose gun.")
            else:
                print("invalid choice. try.again")
    game()
    choice=input("would u like to continue?").lower()
    if choice=='no':
        break
    else:
        game()
