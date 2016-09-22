from Prac08.taxi import Taxi

taxi1 = Taxi("Prius 1", 100)
taxi1.drive(40)
print("{}, current fair cost: ${:.2f}".format(taxi1 ,taxi1.get_fare()))
taxi1.start_fare()
taxi1.drive(100)
print("{}, current fair cost: ${:.2f}".format(taxi1 ,taxi1.get_fare()))