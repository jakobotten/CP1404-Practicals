from Prac08.taxi import Taxi
from Prac08.taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill_to_date = 0
    print("Let's drive!")
    print(MENU)
    menu_selection = input(">>> ")
    while menu_selection != "q":
        if menu_selection == "c":
            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print("{} - {}".format(i, taxi))

            taxi_number = int(input("Choose taxi: "))
            chosen_taxi = taxis[taxi_number]

            print("Bill to date: ${:.2f}".format(bill_to_date))

        elif menu_selection == "d":
            drive_distance = int(input("Drive how far? "))

            chosen_taxi.start_fare()
            chosen_taxi.drive(drive_distance)
            print("Your {} trip cost you ${:.2f}".format(chosen_taxi.name, chosen_taxi.get_fare()))

            bill_to_date += chosen_taxi.get_fare()
            print("Bill to date: ${:.2f}".format(bill_to_date))

        print(MENU)
        menu_selection = input(">>> ")
    print("Total trip cost: ${:.2f}".format(bill_to_date))
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()