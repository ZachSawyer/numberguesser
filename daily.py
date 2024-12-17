import os
import random

def clrscr():
    os.system('cls' if os.name == "nt" else 'clear')

def exit_program():
    clrscr()
    print('Quitting...\nGoodbye!')
    raise SystemExit

def main_menu():
    while True:
        try:
            clrscr()
            user_choice = int(input('Number Guesser\n\n>:1 Play\n>:2 Quit\n'))
            if user_choice == 1:
                difficulty_choice()
                break
            elif user_choice == 2:
                exit_program()
            else:
                clrscr()
                print('Enter 1 to Play or 2 to Quit.\nPress Enter to continue...')
                input()
        except ValueError:
            clrscr()
            print('Enter 1 to Play or 2 to Quit.\nPress Enter to continue...')
            input()

def difficulty_choice():
    while True:
        try:
            clrscr()
            user_choice = int(input('Choose Your Difficulty\n\n>:1 Easy\n>:2 Medium\n>:3 Hard\n'))
            if user_choice == 1:
                easy()
                break
            elif user_choice == 2:
                medium()
                break
            elif user_choice == 3:
                hard()
                break
            else:
                clrscr()
                print('Enter 1 For Easy 2 For Medium or 3 For Hard\nPress Enter to continue...')
                input()
        except ValueError:
            clrscr()
            print('Enter 1 For Easy 2 For Medium or 3 For Hard\nPress Enter to continue...')
            input()

def easy():
    cpuAnswer = random.randrange(1,11)
    userTries = 3
    while True:
        try:
            clrscr()
            user_choice = int(input('I am thinking of a number between 1 and 10...\n\n>:'))
            if user_choice < cpuAnswer:
                clrscr()
                userTries -= 1
                if userTries < 1:
                    print('You Lose!\nPress Enter to continue...')
                    input()
                    play_again()
                    break
                print('Higher')
                print(f'{userTries} guesses left!\nPress Enter to continue...')
                input()
            elif user_choice > cpuAnswer:
                clrscr()
                userTries -= 1
                if userTries < 1:
                    print('You Lose!\nPress Enter to continue...')
                    input()
                    play_again()
                    break
                print('Lower!')
                print(f'{userTries} guesses left!\nPress Enter to continue...')
                input()
            elif user_choice == cpuAnswer:
                clrscr()
                print('You win!\nPress Enter to continue...')
                input()
                play_again()
                break
        except ValueError:
            clrscr()
            print('Enter a number between 1 and 10...\nPress Enter to Continue...')
            input()

def medium():
    cpuAnswer = random.randrange(1,21)
    userTries = 4
    while True:
        try:
            clrscr()
            user_choice = int(input('I am thinking of a number between 1 and 20...\n\n>:'))
            if user_choice < cpuAnswer:
                clrscr()
                userTries -= 1
                if userTries < 1:
                    print('You Lose!\nPress Enter to continue...')
                    input()
                    play_again()
                    break
                print('Higher')
                print(f'{userTries} guesses left!\nPress Enter to continue...')
                input()
            elif user_choice > cpuAnswer:
                clrscr()
                userTries -= 1
                if userTries < 1:
                    print('You Lose!\nPress Enter to continue...')
                    input()
                    play_again()
                    break
                print('Lower!')
                print(f'{userTries} guesses left!\nPress Enter to continue...')
                input()
            elif user_choice == cpuAnswer:
                clrscr()
                print('You win!\nPress Enter to continue...')
                input()
                play_again()
                break
        except ValueError:
            clrscr()
            print('Enter a number between 1 and 20...\nPress Enter to Continue...')
            input()

def hard():
    cpuAnswer = random.randrange(1,31)
    userTries = 5
    while True:
        try:
            clrscr()
            user_choice = int(input('I am thinking of a number between 1 and 30...\n\n>:'))
            if user_choice < cpuAnswer:
                clrscr()
                userTries -= 1
                if userTries < 1:
                    print('You Lose!\nPress Enter to continue...')
                    input()
                    play_again()
                    break
                print('Higher')
                print(f'{userTries} guesses left!\nPress Enter to continue...')
                input()
            elif user_choice > cpuAnswer:
                clrscr()
                userTries -= 1
                if userTries < 1:
                    print('You Lose!\nPress Enter to continue...')
                    input()
                    play_again()
                    break
                print('Lower!')
                print(f'{userTries} guesses left!\nPress Enter to continue...')
                input()
            elif user_choice == cpuAnswer:
                clrscr()
                print('You win!\nPress Enter to continue...')
                input()
                play_again()
                break
        except ValueError:
            clrscr()
            print('Enter a number between 1 and 30...\nPress Enter to Continue...')
            input()

def play_again():
    while True:
        try:
            clrscr()
            user_choice = int(input('Play Again?\n\n>:1 Play\n>:2 Quit\n'))
            if user_choice == 1:
                difficulty_choice()
                break
            elif user_choice == 2:
                exit_program()
            else:
                clrscr()
                print('Enter 1 to Play or 2 to Quit.\nPress Enter to continue...')
                input()
        except ValueError:
            clrscr()
            print('Enter 1 to Play or 2 to Quit.\nPress Enter to continue...')
            input()

def main():
    main_menu()

if __name__ == '__main__':
    main()