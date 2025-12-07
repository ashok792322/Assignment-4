
try:
    with open("Sample.txt",'rt') as fh:
         print("Reading the file content:")
         for line in fh:
           print(line.rstrip('\n'))
except FileNotFoundError:
    print("Error:The file Sample.txt was not found")
