# Import required packages
import shutil
import os

def delete_full_dir_file(dir_path):
    # location
    if os.path.exists(dir_path):
        # removing directory
        shutil.rmtree(dir_path, ignore_errors=False)
        # making ignore_errors = True will not raise a FileNotFoundError
        print("The folder has been deleted successfully!")
    else:
        print("Can not delete the folder as it doesn't exists")

# Usage of the above function
folderPath = "C:/WorkFiles/python demos/my_api_packs/output/samples-main"
delete_full_dir_file(folderPath)
