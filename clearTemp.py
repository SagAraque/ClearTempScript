__author__ = "Sergio Araque García"
__version__ = "1.0"
__status__ = "Production"

import os
import shutil

# Remove directory function
def deleteDir(itemList, tempDir):
    for item in itemList: 
        try:
            shutil.rmtree(os.path.join(tempDir, item))
        except OSError:
            continue

# Remove files function
def deleteFiles(itemList, tempDir):
    for item in itemList: 
        try:
            os.remove(os.path.join(tempDir, item))
        except OSError:
            continue


def clearTemp(tempDir):

    for dirName, subdirList, fileList in os.walk(tempDir, topdown=False):
        # Delete temp files
        deleteDir(subdirList, tempDir)
        # Delete temp dir files
        deleteFiles(fileList, tempDir)




def main():
    clearTemp('TEMP_DIR')
    clearTemp('USER_TEMP_DIR')


if __name__ == '__main__':
    main()