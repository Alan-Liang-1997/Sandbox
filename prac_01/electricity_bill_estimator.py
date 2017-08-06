TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

tariff = float(input("Which tariff? 11 or 31: "))

while tariff != 11 and tariff != 31:

    if tariff == 11:
        tariff = TARIFF_11
    elif tariff == 31:
        tariff = TARIFF_31
    else:
        print("Invalid tariff")
        tariff = float(input("Which tariff? 11 or 31: "))

usage = float(input("Enter daily use in kWh: "))
while usage <= 0:
    print("Invalid daily use")
    usage = float(input("Enter daily use in kWh: "))

period = float(input("Enter number of billing days: "))
while period <= 0:
    print("Invalid number of billing days")
    period = float(input("Enter number of billing days: "))

bill = tariff * usage * period
bill = str(round(bill,2))
print("Estimated bill: $",bill)