# Create a variable, filename. Assuming that it has a three-letter
# extension, and using slice operations, find the extension. For
# README.txt, the extension should be txt. Write code using slice
# operations that will give the name without the extension. Does your
# code work on filenames of arbitrary length?
filename = input("enter the file name: ")
extension = filename.split(".")
print("The extension is: "+extension[-1])
print("the file name without extension is: " + extension[0])
