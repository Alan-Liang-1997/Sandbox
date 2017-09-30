from prac_08.unreliable_car import UnreliableCar

reliable_car = UnreliableCar("Prius 1", 100, 90)
unreliable_car = UnreliableCar("Prius 2", 100, 10)

for i in range(1,10):
    print("Attempting to drive {}km".format(i))
    print("{} drove {}km".format(reliable_car.name, reliable_car.drive(i)))
    print("{} drove {}km".format(unreliable_car.name, unreliable_car.drive(i)))
print()
print(reliable_car)
print(unreliable_car)