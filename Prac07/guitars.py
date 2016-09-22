from Prac07.guitar import Guitar

guitars = []
print("My Guitars!")
while True:
    name = input("Name: ")
    if name == "":
        break
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar = Guitar(name, year, cost)
    guitars += [guitar]
    print("{} added".format(guitar))

print("These are my guitars:")

for count, guitar in enumerate(guitars):
    if guitar.is_vintage():
        vintage_string = "(vintage)"
    else:
        vintage_string = ""
    print("Guitar {}:  {:>8} ({}), worth $ {:8.2f} {}".format(count + 1, guitar.name, guitar.year, guitar.cost, vintage_string))
