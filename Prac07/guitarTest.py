from Prac07.guitar import Guitar

red_guitar = Guitar("Red Guitar", 1936, 1200)
green_guitar = Guitar("Green Guitar", 2011, 999.98)
blue_guitar = Guitar("Blue Guitar", 1816, 13045.50)


print("get_age() - Expected 80. Got {}".format(red_guitar.get_age()))
print("get_age() - Expected 5. Got {}".format(green_guitar.get_age()))
print("get_age() - Expected 200. Got {}".format(blue_guitar.get_age()))

print("is_vintage() - Expected True. Got {}".format(red_guitar.is_vintage()))
print("is_vintage() - Expected False. Got {}".format(green_guitar.is_vintage()))
print("is_vintage() - Expected True. Got {}".format(blue_guitar.is_vintage()))

