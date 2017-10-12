import os
import shutil


def main():
    # Move to desired directory
    os.chdir('FilesToSort')
    print("Current directory is", os.getcwd())

    for dir_name, subdir_list, file_list in os.walk('.'):
        for f in file_list:
            extension = os.path.splitext(f)[1]
            try:
                os.mkdir(extension)
            except FileExistsError:
                pass

            shutil.move(f, extension)

main()
