import re
from pathlib import Path
from datetime import datetime, timedelta
folder = Path.home()/"Pictures"
folder= folder/"Screenshots"
new_f= datetime.now() - timedelta(days=7)
for item in folder.iterdir():
    if not item.is_file():
        continue
    match = re.search(r"\d{4}-\d{2}-\d{2}", item.name)
    if not match:
        continue
    screenshot_date = datetime.strptime(match.group(), "%Y-%m-%d")
    if screenshot_date.date() < new_f.date():
        print(item.name, "too old")
        old= folder/ "old_screenshots"
        old.mkdir(exist_ok=True)
        move=old/item.name
        if not move.exists():
            item.rename(move)
        else:
            counter=1
            move=old/f"{item.stem}_{counter}{item.suffix}"
            while move.exists():
                counter+=1
                move=old/f"{item.stem}_{counter}{item.suffix}"
            item.rename(move)

    else:
        print(item.name,"less than a week old")
        new=folder/"new_screenshots"
        new.mkdir(exist_ok=True)
        move=new/item.name
        if not move.exists():
            item.rename(move)
        else:
            couter=1
            move=new/f"{item.stem}_{counter}{item.suffix}"
            while move.exists():
                counter+=1
                move=new/f"{item.stem}_{counter}{item.suffix}"
            item.rename(move)