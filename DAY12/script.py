import sys


# Check if the correct number of arguments are provided
if len(sys.argv) < 4:
    print("Usage: python script.py <name> <challenge>")
    sys.exit(1)

# Access command line arguments
script_name = sys.argv[0]
first_argument = sys.argv[1]
second_argument = sys.argv[2]
third_argument = sys.argv[3]

# Print the script name and arguments
print('Script name:', script_name)
print('First argument:', first_argument)
print('Second argument:', second_argument)
print('Second argument:', third_argument)

# Format and print a welcome message
print('hello {} {}  enjoy the challenge!'.format(first_argument, second_argument))
print('hello {} {} you will get placed for  sure in well reputed organization with the blessings of {} at first attempt you see this year  '.format(first_argument, second_argument,third_argument))
