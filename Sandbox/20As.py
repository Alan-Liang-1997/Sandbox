"""

With the provided english dictionary create a program that finds the first 20 entries starting with a and 
print the results to a new document.

"""
in_file = open("english_dictionary.txt", "r")
out_file = open("first_20_entries_starting_with_a.txt", "w")
condition = False
number_of_a = 0

while condition is False:
    line_str = in_file.readline()
    if "a" in line_str[0]:
        print(line_str)
        print(line_str, file=out_file)
        number_of_a = number_of_a + 1
        if number_of_a >= 20:
            condition = True

in_file.close()
out_file.close()
