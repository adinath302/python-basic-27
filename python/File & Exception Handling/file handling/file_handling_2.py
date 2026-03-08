# file handling explain -

# 1 -  it allow you to create, read, update, and delete files directly from your code, ensuringg data persistence even after a program stops running.

# 2 - the process of managing the flow of data between a program and files stored on a persistent storage device, such as a hard disk

# ---------------------------------------------------------------------------

# core concepts -

#  open() - the primary way to interact with files
# syntax - file_objcet = open('file_name','mode')

# file_object - it is a variable that represents a file in your program

# mode - file access modes:
# 'r' - read mode - default mode ,fails if file doesn't exist.
# 'w' - write mode -  Overwrites existing content or creates a new file.
# 'a' - append mode - Adds data to the end of the file without overwriting.
# 'x' - exclusive mode - creates a new file if it doesn't exist, throws an error if the file already exists
# 'b' - binary mode - for binary files
# 't' - text mode - for text files
# '+' - update. open for both reading and writing(eg. "r+", "w+", "a+")

# closing files - Essential to release system resources and prevent data corruption.
# Manual closing - file.close()
#
# The "with" statement(best practice): Automatically closes the file even if errors occur

# # ex -
# with open("data.txt", "r") as file:
# content = file.read()
# file is automatically closed here
# ----------------------------------------------------------------
# key methods -
# read(size): Reads the entire file (or size bytes) as a string.
# readline(): Reads a single line.
# readlines(): Reads all lines into a list of strings.
# write(string): Writes text to the file.
# writelines(list): Writes a list of strings at /once.
# tell(): Returns the current cursor position.
# seek(offset): Moves the cursor to a specific position.

# ----------------------------------------------------------------
# practice problems -

arr = open("notes.txt", "w")
arr.write("i love python")
arr.close()

arr1 = open("notes.txt", "r")  # read mode
lw = arr1.read()
arr1.close()

print(lw)


# ----------------------------------------------------------------


# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
# ----------------------------------------------------------------
