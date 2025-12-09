
# Name: Ismael Charly Diarrassouba
# Username: 201952742

# Lists contents of a zip archive
# usage: python ziplist.py <zipfile>
# eg. python ziplist.py testdir/test.zip
# You must use the error messages precisely as defined below.

# Hint: look at the documentation for the "zipfile" module

import sys
#from zipfile import ...   # tools in this module can be used
import zipfile
# filename is a command line argument 
if len(sys.argv) != 2:
    print("Usage: python ziplist.py <filename.zip>", file=sys.stderr)
    sys.exit(1)

file_name = sys.argv[1]
try:
    with zipfile.ZipFile(file_name, 'r') as zip_ref:
        for file in zip_ref.namelist():
            print(file)
    
except FileNotFoundError:
    print(f"File not found: python ziplist.py {file_name}", file=sys.stderr)
    sys.exit(1)

except zipfile.BadZipFile:
    print(f"Bad zip file: python ziplist.py {file_name}", file=sys.stderr)
    sys.exit(1)

except TypeError:
    print(f"Usage: python ziplist.py <filename.zip>", file=sys.stderr)
    sys.exit(1)
# Error message: "Usage: python ziplist.py <filename.zip>"


# Error message: "File not found: python ziplist.py {file_name}"

# Error message: "Bad zip file: python ziplist.py {file_name}"
# Hint: There is an exception for this defined in the zipfile module

# Use zipfile methods to list the contents of the zip file.
# Test your script on the zip_example.zip file. The response should be:
# README.md
# cmd_line.py
# find_file.py
# password.py
# rockpaperscissors.py
