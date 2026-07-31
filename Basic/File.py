f = open("test.txt","w")
f.write("what is your name \nwhere are you from \n")
f.write("i dont know you \nare you a boy")

f= open("test.txt","r")
data= f.read()
print(data)

# deleting file dlt.txt

import os
os.remove("dlt.txt")