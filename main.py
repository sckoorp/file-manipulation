# Reading files
def read_file():
    # Open file
    file = open("users.txt", "r")

    # Read file
    content = file.read()
    print(content)

    # Read file lines
    # lines = file.readlines()

    # for line in lines:
    #    print(line)

    # Close file
    file.close()

# Writing files
def write_file(filename: str):
    # Data to write
    tech_stack = ["TypeScript", "Vue", "Nuxt", "Pocketbase"]

    # Open file
    file = open(filename, "w")

    # Write file
    for i in tech_stack:
        # "\n" new line character
        file.write(i + "\n")

    # Close file
    file.close()

# Write & Read files
def write_read_file(filename: str):
    # Data to write
    groceries = ["Apples", "Bananas", "Oranges", "Peaches"]

    # Open file
    file = open(filename, "w+")

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
    # Data to append
    books = ["Wuthering Heights", "Dune", "The Hobbit"]

    # Open file
    file = open(filename, "a")

    # Append to file
    for i in books:
        # "\n" new line character
        file.write(i + "\n")
    
    # Close file
    file.close()


def main():
    # read_file()
    # write_file("stack.txt")
    # write_read_file("groceries.txt")
    append_to_file("books.txt")
    return

if __name__ == "__main__":
    main()