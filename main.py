from pathlib import Path # pathlib module

# Reading files
def read_file(filename: str):
    # Access path
    dir = Path(__file__).parent

    # File path
    path = dir / filename

    # Open file
    try:
        file = open(path, "r")
        # Read file
        content = file.read()
        print(content)
        # Close file
        file.close()
    except FileNotFoundError:
        print(f"'{filename}' does not exist!")  
    except Exception as e:
        print(f"Unexpected error: {e}")  

    # Read file lines
    # lines = file.readlines()

    # for line in lines:
    #    print(line)

    # Close file
    # file.close()

# Writing files
def write_file(filename: str):
    # Access path
    dir = Path(__file__).parent

    # File path
    path = dir / filename

    # Data to write
    tech_stack = ["TypeScript", "Vue", "Nuxt", "Pocketbase"]

    # Open file
    file = open(path, "w")

    # Write file
    for i in tech_stack:
        # "\n" new line character
        file.write(i + "\n")

    # Close file
    file.close()

# Write & Read files
def write_read_file(filename: str):
    # Access path
    dir = Path(__file__).parent

    # File path
    path = dir / filename

    # Data to write
    groceries = ["Apples", "Bananas", "Oranges", "Peaches"]

    # Open file
    file = open(path, "w+")

    # Write file
    for i in groceries:
        # "\n" new line character
        file.write(i + "\n")
    
    # Reset cursor (if we don't reset cursor it will just return an empty res)
    file.seek(0, 0)

    # Read file
    content = file.read()
    print(content)

    # Close file
    file.close()

# Appending to files
def append_to_file(filename: str):
    # Access path
    dir = Path(__file__).parent

    # File path
    path = dir / filename

    # Data to append
    books = ["Wuthering Heights", "Dune", "The Hobbit"]

    # Open file
    file = open(path, "a")

    # Append to file
    for i in books:
        # "\n" new line character
        file.write(i + "\n")
    
    # Close file
    file.close()

def context_managers(filename: str):
    # Access path
    dir = Path(__file__).parent

    # File path
    path = dir / filename

    # Data to append
    instruments = ["Piano", "Guitar", "Violin"]

    # Context manager ==> Auto closes
    with path.open("w") as file:
        for instrument in instruments:
            # "\n" new line character
            file.write(instrument + "\n")
            

def main():
    # read_file("users.txt")
    # write_file("stack.txt")
    # write_read_file("groceries.txt")
    # append_to_file("books.txt")
    # context_managers("instruments.txt")
    return

if __name__ == "__main__":
    main()