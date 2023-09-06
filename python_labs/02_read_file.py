def read_file_data(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "File not found: %s" % file_path
    except Exception as e:
        return "An error occurred while reading file"

#Usage of above function
file_path = "C:\Tark_Files\WorkFiles\python demos\my_api_packs\source\sample.txt"
file_content = read_file_data(file_path)
if isinstance(file_content, str):
    print(file_content)
else:
    print("Failed to read file: " + file_path)