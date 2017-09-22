"""
CP1404/CP5632 Practical
State names in a dictionary
"""

STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}

state_short_desc = input("Enter short state: ").upper()
while state_short_desc != "":
    if state_short_desc in STATE_NAMES:
        print(state_short_desc, "is", STATE_NAMES[state_short_desc])
    else:
        print("Invalid short state")
    state_short_desc = input("Enter short state: ").upper()

for short_state_desc, full_state in STATE_NAMES.items():
    print("{:<3} is {:<10}".format(short_state_desc, full_state))
