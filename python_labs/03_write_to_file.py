def write_data_to_file(file_path, content):
    try:
        with open(file_path, 'w+') as file:
            file.write(content)
        return file_path
    except FileNotFoundError:
        return "File not found: %s" % file_path
    except Exception as e:
        return "An error occurred while reading file"
#Usage of above function
my_content = "file_content will come here to test the working script"
file_path = "C:\Tark_Files\WorkFiles\python demos\my_api_packs\source\sample2.txt"
result = write_data_to_file(file_path, my_content)
if result == file_path:
    print ("File has been successfully created")
else:
    print ("Could not write to file")