with open ("practise.txt","w") as f :
    f.write("what is your name \nwhere are you from\n")
    f.write("what is your town \nok do it\n")

with open("practise.txt","r") as f:
    data= f.read()
    ndata= data.replace("is","ok")
    print(ndata)
