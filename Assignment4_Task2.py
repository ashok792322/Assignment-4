#open and write
fh = open("output.txt",'wt')
fh.write(input("Enter text to write to file: "))
fh.write("\n")
fh.close()
print("Data successfully written to output.txt\n")
# Appending
fh = open("output.txt",'at')
fh.write(input("Enter additional text to append: "))
fh.write("\n")
fh.close()
print("Data successfully append.\n")

# Displaying output
fh=open("output.txt",'rt')
content = fh.read()
print(f"Final content of output.txt:\n{content.rstrip('\n')}")
#closing open file
fh.close()





