# Description

Utility for reverting and/or uppercaseing a string from a command line input or from file.

# Example usage
### Input string from cmd
cmd input: python reverse_and_uppercase.py test string
cmd output: GNIRTS TSET

cmd input: python reverse_and_uppercase.py test string -u
cmd output: TEST STRING

cmd input: python reverse_and_uppercase.py test string -r
cmd output: gnirts tset

### Input from file
Let us have a file named 'test_file.txt' with the containg two following lines.
test1
test2

Reverse_and_uppercase.py utility may be used in a following way.
cmd input: python reverse_and_uppercase.py -f test_file.txt -u

Output file will be named 'test_file_processed.txt' and will contain following two lines.
TEST1
TEST2