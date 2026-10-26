from pathlib import Path
l=[]
folder = Path.home()/"Downloads"/"mods"
for item in folder.iterdir():
    l.append(item.name)
print(l)