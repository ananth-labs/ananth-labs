import shutil
import os

# location
folderPath = "C:/Tark_Files/WorkFiles/python demos/my_api_packs/output/samples-main"
if os.path.exists(folderPath):
    # removing directory
    shutil.rmtree(folderPath, ignore_errors=False)
    # making ignore_errors = True will not raise a FileNotFoundError
    print("The folder has been deleted successfully!")
else:
    print("Can not delete the folder as it doesn't exists")