"""
CP1404/CP5632 Practical
File renaming and os examples
"""
# import shutil
import os


def main():
    """Demo file renaming with the os module."""
    print("Current directory is", os.getcwd())

    # change to desired directory
    os.chdir('Lyrics/Christmas')
    # print a list of all files (test)
    print(os.listdir('.'))

    # make a new directory
    # os.mkdir('temp')

    # loop through each file in the (original) directory
    for filename in os.listdir('.'):
        # ignore directories, just process files
        if not os.path.isdir(filename):
            new_name = get_fixed_filename(filename)
            print(new_name)

            # Option 1: rename file to new name - in place
            # os.rename(filename, new_name)

            # Option 2: move file to new place, with new name
            # shutil.move(filename, 'temp/' + new_name)

            # Processing subdirectories using os.walk()
            # os.chdir('..')  # .. means "up" one directory
            # for dir_name, subdir_list, file_list in os.walk('.'):
            #     print("In", dir_name)
            #     print("\tcontains subdirectories:", subdir_list)
            #     print("\tand files:", file_list)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    # First, replace the spaces and .TXT (the easy part)
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    new_name = new_name[0].upper() + new_name[1:]

    # Second, replace PascalCase. i.e. SilentNight
    pascal_name = new_name[0]
    for index, character in enumerate(new_name[1:]):
        # If current character is uppercase, and the previous character is lowercase and not a underscore
        if character.isupper() and new_name[index-1].islower() and not new_name[index] == "_":
            pascal_name += "_" + character
        else:
            pascal_name += character

    # Third, replace names not in TitleCase. i.e. O little town of bethlehem
    title_name = pascal_name[0]
    for index, character in enumerate(pascal_name[1:]):
        # Check if character is lowercase and if character is _
        if character.islower() and pascal_name[index] == "_":
            title_name += character.upper()
        else:
            title_name += character
    # All cases have been considered, output final_name
    final_name = title_name
    return final_name


main()
