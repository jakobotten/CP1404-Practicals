from Prac07.car import Car


def main():
    bus = Car("bus", 100)
    bus.drive(30)
    print(bus)

    limo = Car("limo", 100)
    limo.add_fuel(20)
    print(limo)
    limo.drive(115)
    print(limo)
main()
