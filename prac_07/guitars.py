from prac_07.guitar import Guitar


def main():
    # Create guitars list for storing
    guitars = []

    print("My Guitars!")
    print("Enter blank name to show guitar list and exit!")
    name = str(input("Name: "))
    # Loop as long as user does not input empty name
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_info = Guitar(name, year, cost)
        print("{self.name} ({self.year}) : ${self.cost:.2f} added.".format(self=guitar_info))
        guitars.append(guitar_info)
        # Restart Loop
        name = input("Name: ")

    # Exit Loop
    print("... snip ...")
    # Add some guitars for data
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    # Start print guitar list process
    print("These are my guitars:")
    longest_name = max(len(guitar.name) for guitar in guitars)
    longest_year = max(len("{:.2f}".format(guitar.year)) for guitar in guitars)
    longest_cost = max(len("{:.2f}".format(guitar.cost)) for guitar in guitars)

    for index, guitar in enumerate(guitars):
        if guitar.is_vintage():
            vintage_status = "(vintage)"
        else:
            vintage_status = ""

        print("Guitar {0}: {self.name:>{1}} {self.year:>{2}}, worth "
              "${self.cost:<{3},.2f} {4}".format(index + 1, longest_name, longest_year, longest_cost, vintage_status,
                                                 self=guitar))


main()
