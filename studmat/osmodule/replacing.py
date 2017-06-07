import os
import string
def replace(file, search_for, replace_with):
   temp = os.path.splitext(file)[0] + ".tmp"
   try:
        os.remove(temp)
   except os.error:
        pass
   fi = open(file)
   fo = open(temp, "w")
   for s in fi.readlines():
        fo.write(string.replace(s, search_for, replace_with))
   fi.close()
   fo.close()
file = "samples/sample.txt"
replace(file, "hello", "tjena")





