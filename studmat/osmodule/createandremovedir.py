import os

#os.makedirs("test1/multiple1/levels1")

#fp = open("test1/multiple1/levels1/file", "w")
#fp.write("inspector praline")
#fp.close()

# remove the file
os.remove("test1/multiple1/levels1/file")

# and all empty directories above it
os.removedirs("test1/multiple1/levels1")
