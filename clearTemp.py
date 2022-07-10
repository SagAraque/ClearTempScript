__author__ = "Sergio Araque García"
__version__ = "1.1"
__status__ = "Production"

import os
import shutil

# Remove directory and files function
def delete(itemList, tempDir):
    for item in itemList: 
        path = os.path.join(tempDir, item)
        try:
            os.remove(path) if os.path.isfile(path) else shutil.rmtree(path)
        except OSError:
            continue



def clearTemp(tempDir):

    for dirName, subdirList, fileList in os.walk(tempDir, topdown=False):
        # Delete temp files
        delete(subdirList, tempDir)
        # Delete temp dir files
        delete(fileList, tempDir)



def main():
    clearTemp('TEMP_DIR')
    clearTemp('USER_TEMP_DIR')


if __name__ == '__main__':
    main()