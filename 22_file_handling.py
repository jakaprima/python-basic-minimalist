import os

current_dir = os.getcwd()
file_name = '22_file_data.txt'
file_path = f'{current_dir}/{file_name}'

"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"""
# ------------------------------------------------------------create file
try:
    with open(file_path, 'x'):
        print("FILE CREATED")
except FileExistsError:
    print("FILE EXIST")

# ------------------------------------------------------------CHECK file
if os.path.exists(file_path):
    print("FILE EXISTS")
else:
    print("FILE NOT EXISTS")

# with open(file_path, 'a') as file_data:
#     file_data.write('this line wil be added if the file is created')


"""
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
"""
# ------------------------------------------------------------read file
with open(file_path, 'rt') as file_data:
    print(file_data.read())

# ------------------------------------------------------------write file
with open(file_path, 'w') as file_data:
    file_data.write("HALO DUNIA")

# ------------------------------------------------------------read file and back to pointer beginning again 
with open(file_path, 'rt') as file_data:
   # Read the entire contents of the file
    text_data = file_data.read()
    print(text_data)

    # Move the pointer back to the beginning of the file
    file_data.seek(0)

    # Return the first 5 characters
    first_five_chars = file_data.read(5)
    
    print("RETURN 5 first chars:", first_five_chars)
    # read one line 
    file_data.readline()

with open(file_path, 'a') as file_data:
    file_data.write(" APPEND NEW TEXT ")

with open(file_path, 'rt') as file_data:
    print(file_data.read())
    

# ------------------------------------------------------------delete file
# os.remove(file_path)