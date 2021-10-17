"""
CP1404 Practical 09
Extended file extension sorting program
Henry Vooren
"""

import shutil
import os


directories = []
dictionary = {}


def main():
    """shutil move method to move files to extension determined directories"""
    os.chdir('FilesToSort')

    for filename in os.listdir():
        file_parts = filename.rsplit('.')
        extension = file_parts[1]
        if not(extension in directories):
            folder = input(f"What folder would you like to sort files with extension {extension} into? ")
            try:
                os.mkdir(folder)
            except FileExistsError:
                pass

            directories.append(extension)  # directory appended outside of try method
            # as folder directory may exist while extension has not been previously saved
            dictionary[extension] = folder  # making file extension the key saves having to make another for loop

            shutil.move(filename, folder)
        else:
            """Using dict for file extension/folder mapping"""
            shutil.move(filename, dictionary[extension])


main()
