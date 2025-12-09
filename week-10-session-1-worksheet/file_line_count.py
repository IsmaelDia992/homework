
# Name: Ismael Charly Diarrassouba
# Username: 201952742

import sys

# Show the number of non-empty lines in a text file
# Usage: python file_line_count.py <filename>
# Example: python file_line_count.py textexample.txt
# You must use the error messages precisely as defied below.

# filename is a command line argument 

# count number of lines that are not blank
number_of_lines = 0

if len(sys.argv) != 2:
    print("Usage: python file_line_count.py <filename.txt>", file=sys.stderr)
    sys.exit(1)

file_name = sys.argv[1]

try:
    with open (f"{file_name}", "r") as f:
        for line in f:
            if line.strip() != "":
                number_of_lines = number_of_lines + 1
        print(f"{file_name} has {number_of_lines} lines")
        





# Error message: "Usage: python file_line_count.py <filename.txt>"

# Error message: "File not found: python file_line_count.py {file_name}" done
except FileNotFoundError:
    print(f"File not found: python file_line_count.py {file_name}", file=sys.stderr)
    sys.exit(1)

except TypeError:
    print(f"Usage: python file_line_count.py <filename.txt>", file=sys.stderr)
    sys.exit(1)


# Test on the 'text_example.txt' file. The answer should be 4.