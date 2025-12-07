# ASSIGNMENT 4:
## Module 5: Files, Exceptions, and Errors in Python
 
### Task 1: Read a File and Handle Errors 
### Problem Statement:  Write a Python program that:
### 1.   Opens and reads a text file named sample.txt.
### 2.   Prints its content line by line.
### 3.   Handles errors gracefully if the file does not exist.<br><br>

                                                                                                    
### try:
### with open("Sample.txt",'rt') as fh:
opening file using open() having 1st argument as file name Sample.txt and 2nd argument rt i.e read and text mode and resultant file object assign to variable fh. with statement used for automatic file closer eighter in case of completion of read operation or any error occur
 try block is used so that if file not found error occur will be handle by except block. 

### print("Reading the file content:")
print() for printing message that displaying content of file Sample.txt

         
### for line in fh:
### print(line.rstrip('\n'))
for loop used for printing line by line content of file by taking variable line as iteration taking data from file object fh and than printing each line using print() taking argument as variable line using with rstrip('\n') to remove new line character  from right of line on each iteration.

### except FileNotFoundError:
### print("Error:The file Sample.txt was not found")
except block aspect error from try block . And specific error mentioned in except block will capture that error and message mentioned in print() will be printed. <br><br><br>
# Assignment 4
## Task 2: Write and Append Data to a File<br>
 
### Problem Statement: Write a Python program that:
### 1.   Takes user input and writes it to a file named output.txt.
### 2.   Appends additional data to the same file.
### 3.   Reads and displays the final content of the file.<br><br>


## opening and writing to file

### fh = open("output.txt",'wt')
To write in file output.txt it is open using open() having 1st argument the file name output.txt and 2nd argument  write and text mode  and resultant file handler assign to variable fh.
if file output.txt not exist than w mode will create file in name of output.txt
if file output.txt exist the previous content will be truncated and allow fresh content to write from next line of code.

### fh.write(input("Enter text to write to file: "))
To write content in output.txt, file hander fh is used with write() having argument as string by user input through input().

### fh.write("\n")
To add next line file handler fh  is used with write() having argument '\n' string used for new line so that next content start from new line.

### fh.close()
file handler fh used to close the file for write operation by using close()

### print("Data successfully written to output.txt\n")
print() used to display message that data successfully written to file.


## Appending

### fh = open("output.txt",'at')
To append in file output.txt it is open using open() having 1st argument the file name output.txt and 2nd argument as  append  and text mode  and resultant file handler assign to variable fh.
Here previous variable fh overwritten by new file object.
in a mode content will be added to the end of previous content of file output.txt.

### fh.write(input("Enter additional text to append: "))
To append content in output.txt, file hander fh is used with write() having argument as string by user input through input().

### fh.write("\n")
To add next line file handler fh  is used with write() having argument '\n' string used for new line so that next content start from new line.

### print("Data successfully append.\n")
print() used to display message that data successfully append to file.

### fh.close()
file handler fh used to close the file for append opeartion by using close()


## Displaying output
### fh=open("output.txt",'rt')
finally content store in file output.txt is displayed by opening file using open() having 1st argument file name output.txt and 2nd argument rt i.e read and text mode and resultant file object assign to variable fh.
Here once again previous variable fh overwritten by new file object, as same name fh for variable file handler used.

### content = fh.read()
file handler fh used with read() to read the entire content of output.txt and save in variable content as string.

### print(f"Final content of output.txt:\n{content.rstrip('\n')}")
content of file output.txt displayed by print() using fstring  for strings for understanding for respected variable content along with accessing rstrip() to delete new line character from right from line of string. 

## closing open file

### fh.close()
file handler fh used to close the file for read operation by using close()
