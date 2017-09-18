"""
CP1404/CP5632 Practical
State names in a dictionary
"""

STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}

full_state = input("Enter short state: ").upper()
while full_state != "":
    if full_state in STATE_NAMES:
        print(full_state, "is", STATE_NAMES[full_state])
    else:
        print("Invalid short state")
    full_state = input("Enter short state: ").upper()

for short_state, full_state in STATE_NAMES.items():
    print("{:<3} is {:<10}".format(short_state, full_state))
