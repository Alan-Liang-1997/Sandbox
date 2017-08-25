"""
CP1404/CP5632 - Assignment 1
Alan Liang - 13179642
"""
MENU = """L - List songs
A - Add new song
C - Complete a song
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            list_songs()
        elif choice == "A":
            add_song()
        elif choice == "C":
            complete_song()
        else:
            print("Invalid menu choice.")
        print(MENU)
        choice = input(">>> ").upper()

    print("Have a nice day :)")


def list_songs():
    print()


def add_song():
    print()


def complete_song():
    print()



main()