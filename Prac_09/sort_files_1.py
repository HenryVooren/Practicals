"""
CP1404 Practical 09
Simple file extension sorting program
Henry Vooren
"""

import shutil
import os


directories = []


def main():
    """shutil move method to move files to extension determined directories"""
    os.chdir('FilesToSort')

    for filename in os.listdir():
        file_parts = filename.rsplit('.')
        extension = file_parts[1]
        if not(extension in directories):
            try:
                os.mkdir(extension)
                directories.append(extension)  # directories listing inside try method
                # as on fail extension exists within directory
            except FileExistsError:
                pass

        shutil.move(filename, extension)


main()
