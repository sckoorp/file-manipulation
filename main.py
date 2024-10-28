# Reading files
def read_file():
    # Open file
    file = open("users.txt", "r")

    # Read file
    # content = file.read()
    # print(content)

    # Read file lines
    lines = file.readlines()

    for line in lines:
        print(line)

    # Close file
    file.close()

def main():
    read_file()
    return

if __name__ == "__main__":
    main()