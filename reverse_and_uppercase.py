import sys

try:
    input_string = sys.argv[1][::-1].upper()
    print("Reversed input string in the uppercase is: %s" % input_string)
except:
    print("The program must be run from the comand line as: python reverse_and_uppercase.py \"string to reverse\" ")
    e = sys.exc_info()
    print("Error", e)