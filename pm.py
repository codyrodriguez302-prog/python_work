"""
height = 65
gender = "female"

if height < 62 or (height < 69 and gender == "male"):
    print("You are below average height")
elif height > 69 or (height > 62 and gender == "female"):
    print("You are above average height")
else:
    print("You are average height")
"""\

names_list=["pepe","Asul", "jose"]
names=" ".join(names_list)
print(names)