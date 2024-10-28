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

def main():
    # read_file()
    write_file("stack.txt")
    return

if __name__ == "__main__":
    main()