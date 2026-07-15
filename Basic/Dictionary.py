# methods

info= {
    "name" : "abid",
    "age" : "34",
    "sub" : ["phy","chm"],
    "gpa" : {
        "class1" : "a",
        "class2" : "b",
        "class3" : "c",
        "class4" : "d",
    }
}

print(info)

info["name"]="AK"
print(info["name"])

print(info.keys())
print(info.values())
print(info.items())
print(info.get("age"))
info.update({"age" : "35" })

print(info)





