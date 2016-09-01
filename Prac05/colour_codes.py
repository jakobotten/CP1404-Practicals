COLOUR_HEX_VALUE = {"BROWN": "#a52a2a", "CHOCOLATE": "#d2691e", "BURLYWOOD": "#deb887", "DARKORANGE": "#ff8c00",
                    "TAN": "#d2b48c", "SADDLEBROWN": "#8b4513", "OLIVEDRAB": "#6b8e23", "INDIANRED": "#cd5c5c",
                    "HOTPINK": "#ff69b4", "GRAY": "#bebebe"}

colour = input("Enter colour name: ").upper()
while colour != "":
    if colour in COLOUR_HEX_VALUE:
        print("Hex value for the colour", colour.capitalize(), "is", COLOUR_HEX_VALUE[colour])
    else:
        print("Invalid colour name")
    state = input("Enter colour name: ").upper()
