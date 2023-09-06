import sys
import zipfile

def count_lines(file_path):
    try:
        # Open the file for reading
        with open(file_path, 'r') as file:
            # Initialize a line counter
            line_count = 0
            # Iterate through each line in the file
            for line in file:
                line_count += 1

        # Print the total number of lines
        print(f'Total number of lines in the file: {line_count}')

    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def count_files(zip_file_path):
    try:
        # Open the zip file
        with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
            # List all the files in the zip folder
            file_list = zip_file.namelist()
            
            # Count the number of files
            num_files = len(file_list)
            
            # Print the list of files (optional)
            print("Files in the zip folder:")
            for file in file_list:
                print(file)

        # Print the total number of files
        print(f'Total number of files in the zip folder: {num_files}')

    except FileNotFoundError:
        print(f"The file {zip_file_path} was not found.")
    except zipfile.BadZipFile:
        print(f"The file {zip_file_path} is not a valid zip file.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if len(sys.argv) != 3:
    print("Usage: python count.py <option> <file_path>")
    print("Options: -t for text file, -z for zip file")
    sys.exit(1)

option = sys.argv[1]
file_path = sys.argv[2]

if option == '-t':
    count_lines(file_path)
elif option == '-z':
    count_files(file_path)
else:
    print("Invalid option. Use -t for text file or -z for zip file.")
