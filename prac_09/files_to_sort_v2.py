import os
import shutil


def main():
    # Move to desired directory
    os.chdir('FilesToSort')
    print("Current directory is", os.getcwd())

    for dir_name, subdir_list, file_list in os.walk('.'):
        extensions_to_folders_dict = {}
        for f in file_list:
            extension = os.path.splitext(f)[-1]
            key_exists = False
            for key in extensions_to_folders_dict:
                # If file extension already exists, skip creating overlapping category
                if key == extension:
                    key_exists = True

            # Else, If file extension has not been sorted, prompt user
            if not key_exists:
                category = input("What category would you like to sort {} files into? ".format(extension))
                extensions_to_folders_dict[extension] = category
            category = extensions_to_folders_dict[extension]
            try:
                os.mkdir(category)
            except FileExistsError:
                pass

            shutil.move(f, category)

main()
