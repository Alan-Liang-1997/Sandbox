from prac_08.silver_service_taxi import SilverServiceTaxi

taxi = SilverServiceTaxi("Silver Service Taxi", 100, 2)
taxi.drive(18)
print(taxi)
print()
print("This trip costed: ${}".format(taxi.get_fare()))
