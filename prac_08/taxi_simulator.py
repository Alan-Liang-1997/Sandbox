"""
CP1404/CP5632 Practical
Taxi simulator
"""
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = """
Q - Quit
C - Choose Taxi
D - Drive"""


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    total_bill = 0
    print("Let's drive!")
    print(MENU)

    menu_choice = str(input(">>> ").lower())
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxi's Available:")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            chosen_taxi = taxis[taxi_choice]
            print("Currently chosen taxi: {}".format(chosen_taxi.name))

        elif menu_choice == "d":
            chosen_taxi.start_fare()
            distance_to_drive = int(input("Drive how far? "))
            chosen_taxi.drive(distance_to_drive)
            trip_cost = chosen_taxi.get_fare()
            print("This trip costed ${} using a {}".format(trip_cost, chosen_taxi.name))
            total_bill += trip_cost
        else:
            print("Invalid Input")
        print("Bill to date: ${:.2f}".format(total_bill))
        print(MENU)
        menu_choice = input(">>> ").lower()
    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} = {}".format(i, str(taxi)))

main()
