"""
CP1404/CP5632 Practical
Colour hex values in a dictionary
"""

COLOUR_NAMES = {"AliceBlue": "f0f8ff", "Black": "000000", "DarkGreen": "006400", "DarkOrchid": "9932cc",
                "DodgerBlue1": "1e90ff", "firebrick1": "ff3030", "gold1": "ffd700", "cyan1": "00ffff",
                "coral2": "ee6a50", "chartreuse1": "7fff00"}

colour = input("Enter colour: ")
while colour != "":
    if colour in COLOUR_NAMES:
        print(colour, "is", COLOUR_NAMES[colour])
    else:
        print("Invalid colour")
    colour = input("Enter colour: ")

for colour, hex_value in COLOUR_NAMES.items():
    print("{:<12} is {:<6}".format(colour, hex_value))
