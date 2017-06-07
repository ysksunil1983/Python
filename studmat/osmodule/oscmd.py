import os
cwd = os.getcwd()
print("1",cwd)
os.chdir("samples")
if os.name == "nt":
    command = "ipconfig"
else:
    command = "ls -l"
print(os.name)
print (os.system(command))
