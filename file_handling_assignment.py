try:
    #Creating file in write mode
    file = open("my_file.txt", "w")
    #Writing to file
    file.write("This is line 1.\n")
    file.write("This is line 2.\n")
    file.write("This is ine 3.\n")
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
finally:
    print("Finished writing to file.")

try:
    #Enhanced script reading contents of file
    file = open("my_file.txt", "r")
    print("Contents of 'my_file.txt':")
    print(file.read)
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")

try: 
    #Appending to file
    file = open("my_file.txt", "a")
    file.write("This is the first appended line.")
    file.write("This is the second appended line.")
    file.write("This is the third appended line.")
except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
finally:
    print("Finished appending to file.")