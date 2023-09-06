import re

# Creating a function to replace the text
def replacetext(source_file, search_text,replace_text):

	# Opening the file in read and write mode
	with open(source_file,'r+') as f:

		# Reading the file data and store it in a file variable
		file = f.read()
		
		# Replacing the pattern with the string in the file data
		file = re.sub(search_text, replace_text, file)

		# Setting the position to the top of the page to insert data
		f.seek(0)
		
		# Writing replaced data in the file
		f.write(file)

		# Truncating the file size
		f.truncate()

	# Return "Text replaced" string
	return "String successfully replaced"

# File to search and replace string
file_path = "C:\Tark_Files\WorkFiles\python demos\my_api_packs\source\sample1.txt"

# Creating a variable and storing the text that we want to search
search_text = "one"

#Creating a variable and storing the text that we want to update
replace_text = "two"

# Calling the replacetext function and printing the returned statement
print(replacetext(file_path, search_text,replace_text))
