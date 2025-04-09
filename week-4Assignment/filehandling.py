def file_handling_assignment():
    # File read and write 
    print("\n--- File Read and Write Challenge ---")
    
    try:
        # 1. Open the original file for reading 
        with open('original.txt', 'r') as original_file:
            # 2. Read the entire content of the file
            content = original_file.read()
            print("Original file content:")
            print(content)
            
            # Modify the content (convert to uppercase in this example)
            modified_content = content.upper()
            
            # 3. Open a new file for writing the modified content
            with open('modified.txt', 'w') as modified_file:
                # 4. Write the modified content to the new file
                modified_file.write(modified_content)
                print("\nModified content written to 'modified.txt'")
                print("Check the folder for your new file!")
    
    # ERROR HANDLING
    except FileNotFoundError:
        # If the original.txt does not exist
        print("Error: The file 'original.txt' was not found.")
        print("Please create 'original.txt' in the same folder as this script.")
    except IOError:
        # Other input/output errors (like disk full, no permissions)
        print("Error: Could not read/write the file.")
    except Exception as e:
        # Any other unexpected errors
        print(f"An unexpected error occurred: {str(e)}")
        
        
        
        
        
        
    # PART 2: ERROR HANDLING LAB
print("\n--- Error Handling Lab ---")
print("Now let's try reading any file you want.")

while True:
    # Ask for a file name
    filename = input("\nEnter a filename to read (or 'quit' to exit): ")

    # Check if user wants to quit
    if filename.lower() == 'quit':
        print("Goodbye!")
        break

    try:
        # Try to open and read the user's file
        with open(filename, 'r') as user_file:
            # If successful, print the file contents
            print(f"\nContents of '{filename}':")
            print(user_file.read())
            print("\nFile read successfully!")
            break

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        print("Please check the spelling and try again.")

    except PermissionError:
        print(f"Error: You don't have permission to read '{filename}'.")
        print("Try choosing a different file or checking permissions.")

    except IsADirectoryError:
        print(f"Error: '{filename}' is a directory, not a file.")
        print("Please enter a filename, not a folder name.")

    except Exception as e:
        # Catch-all for any other unexpected errors
        print(f"An unexpected error occurred: {str(e)}")
        print("Please try a different file.")

if __name__ == "__main__":
    print("=== File Handling Program ===")    
file_handling_assignment()

