import zipfile
def unzip_api_pack(apiPackage, destinationfolder):
    with zipfile.ZipFile(apiPackage, 'r') as zip_ref:
        zip_ref.extractall(destinationfolder)
    print ("FIle extracted successfully")

#Usage of above function
print ("Preparing to extract files")
print ("Any files starting with a will through error...")
apizipfile = "C:\Tark_Files\WorkFiles\python demos\my_api_packs\source\my_apigee-samples-main.zip"
outputdir = "C:\Tark_Files\WorkFiles\python demos\my_api_packs\output\samples-main"
unzip_api_pack(apizipfile, outputdir)