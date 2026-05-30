f = open("test.docx", "w")

f.write("HI there viewers")
f.close()

# after every closure rewrite assign te file to a variable
f = open("test.docx", "r")
print(f.read(),"\n")
f.close()

# deleting the same file 
import os
os.remove("test.docx")
print("File has been deleted after output")