import sys


def read(filepath, option):
    """
    Read content from a file based on the given option.

    Args:
        filepath (str): Path of the file to read.
        option (str or int):
            - "all" or "ALL" or "All" to read the entire content.
            - "line" or "LINE" or "Line" to read the first line.
            - "lines" or "LINES" or "Lines" to read all lines.
            - An integer to read a specific number of characters from the file.
            - Any other value to return an error message.
    """
    print("#" * 50)
    try:
        file = open(f"{filepath}", "r")
        # print(filepath)
        if file.readable():
            if option == "all" or option == "ALL" or option == "All":
                return file.read()

            elif option == "line" or option == "LINE" or option == "Line":
                return file.readline()

            elif option == "lines" or option == "LINES" or option == "Lines":
                return file.readlines()

            elif isinstance(option, int):
                return file.read(option)

            else:
                return "Invalid option"
        print()
    except:
        print(sys.exc_info()[1])
    finally:
        file.close()
        print("#" * 50)


def write(filepath, centent):
    """
    Write content to a file.

    Args:
        filepath (str): Path of the file to write to.
        centent (str or list): Content to write to the file.
    Returns:
        str: Message indicating the success or failure of the operation.
    """
    print("#" * 50)
    try:
        file = open(f"{filepath}", "w")
        # print(filepath)
        if file.writable():
            if isinstance(centent, str):
                file.write(centent)
                return "Content written successfully"

            elif isinstance(centent, list):
                file.writelines(centent)
                return "Content written successfully"

            else:
                return "Invalid content"
        print()
    except:
        print(sys.exc_info()[1])
    finally:
        file.close()
        print("#" * 50)


def append(filepath, newcentent):
    """
    Append content to a file.

    Args:
        filepath (str): Path of the file to append to.
        newcentent (str or list): Content to append to the file.
    Returns:
        str: Message indicating the success or failure of the operation.
    """
    print("#" * 50)
    try:
        file = open(f"{filepath}", "a")

        if file.writable():
            if isinstance(newcentent, str):
                file.write(newcentent)
                return "Content written successfully"

            elif isinstance(newcentent, list):
                file.writelines(newcentent)
                return "Content written successfully"

            else:
                return "Invalid content"
        print()
    except:
        print(sys.exc_info()[1])
    finally:
        file.close()
        print("#" * 50)
