import sys, os, subprocess, time, random

IS_WINDOWS = os.name == "nt"
IS_MAC = sys.platform == "darwin"

def clear_screen():
    if IS_WINDOWS:
        os.system("cls")
    else:
        os.system("clear")

def user_choice():
    return input("\n>>> ").lower().strip()

def main():
    clear_screen()
    print("==================\n"
          "  Santa's Little  \n"
          "      Helper      \n"
          "==================\n")
    print("1. Play")
    print("0. Exit")
    choice = user_choice()
    if choice == "1":
        play()
    if choice == "0":
        clear_screen()
        print("Merry Christmas (2017)")
        sys.exit()

def play():
    clear_screen()
    print("YOU : What?!?!?! where am i?")
    input("\nEnter")
    clear_screen()
    print("SANTA : Hello i am santa! i have chosen you to be my helper this christmas!")
    input("\nEnter")
    clear_screen()
    print("SANTA : Your job will be to help me to deliver all of these presents to all the kiddies out there!")
    input("\nEnter")
    clear_screen()
    print("* Santa turns u into an elf *")
    input("\nEnter")
    clear_screen()
    print("Get Delivering!")
    input("\nEnter")
    stage1()

def stage1():
    clear_screen()
    print("===========\n"
          "  Stage 1  \n"
          "===========\n")
    input("\nEnter")
    clear_screen()
    print("House 1 : You head upstairs but the kid sleeping in his room wakes up what will you do?!?!?!?")
    print("\n"
          "1. Run Away  | 2. Scare the kid  | 3. Sneak")
    choice = user_choice()
    if choice == "1":
        clear_screen()
        input("Santa is angry You Loose!")
        main()
    if choice == "2":
        clear_screen()
        print("Great Work you scared the kid which made him hide under his covers!")
        input("\nEnter")
        stage2()
    if choice == "3":
        clear_screen()
        print("WOW! i mean wow... you have good ninja skills!")
        input("\nEnter")
        stage2()

def stage2():
    clear_screen()
    print("===========\n"
          "  Stage 2  \n"
          "===========\n")
    input("\nEnter")
    clear_screen()
    print("House 2 : You Smash a vase!!! What do you do?")
    print("\n"
          "1. Hide and Sneak  | 2. Sprint  | 3. Throw the present")
    choice = user_choice()
    if choice == "1":
        clear_screen()
        input("You Sneak at the wrong time and get caught!")
        main()
    if choice == "2":
        clear_screen()
        print("Good Work! You just made it to the tree!")
        input("\nEnter")
        stage3()
    if choice == "3":
        clear_screen()
        input("The Present Smashes you Loose!")
        main()

def stage3():
    clear_screen()
    print("===========\n"
          "  Stage 3  \n"
          "===========\n")
    input("\nEnter")
    clear_screen()
    print("House 3 : You didnt sleep last night! What will you do?")
    print("\n"
          "1. Drink Coffee  | 2. Quick Nap  | 3. Get Over it")
    choice = user_choice()
    if choice == "1":
        clear_screen()
        input("Oh No! Its not coffee its bleach You Loose!")
        main()
    if choice == "2":
        clear_screen()
        print("You Get away with it and deliver the present!")
        input("\nEnter")
        stage4()
    if choice == "3":
        clear_screen()
        input("You Crash You Loose!")
        main()

def stage4():
    clear_screen()
    print("===========\n"
          "  Stage 4  \n"
          "===========\n")
    input("\nEnter")
    clear_screen()
    print("House 4 : The house alarm goes off! What will you do?")
    print("\n"
          "1. Sprint  | 2. Come Back Later  | 3. Hide and run")
    choice = user_choice()
    if choice == "1":
        clear_screen()
        input("You get caught You Loose!")
        main()
    if choice == "2":
        clear_screen()
        input("It is morning when you get back You Loose!")
        main()
    if choice == "3":
        clear_screen()
        print("You made it to the tree!")
        input("\nEnter")
        final()

def final():
    clear_screen()
    print("============\n"
          "    Final   \n"
          "============\n")
    input("\nEnter")
    clear_screen()
    print("Final House : You trigger an alarm that was setup by the kid")
    print("\n"
          "1. Run to Tree  | 2. Use invisibility Cloak  | 3. Take a nap")
    choice = user_choice()
    if choice == "1":
        input("Merry Christmas From ArtGames! 2017")
        main()
    if choice == "2":
        input("Merry Christmas From ArtGames! 2017")
        main()
    if choice == "3":
        input("Merry Christmas From ArtGames! 2017")
        main()

main()
