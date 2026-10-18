
from pathlib import Path
folder = Path.home() / "Downloads"
print(folder)
image_format={".jpg",".jpeg",".png",".gif",".webp",".bmp",
".tif",".tiff",".svg",".heic",".heif",".avif",".ico",".raw",".dng",".jfif",}
def move_file(item, target_folder):
    target_folder.mkdir(exist_ok=True)
    destination= target_folder/item.name
    if not destination.exists():
        print("safe to move")
        item.rename(destination)
    else:
        print("item already exist")
        counter=1
        print(f"{item.stem}_{counter}{item.suffix}")
        destination=target_folder/f"{item.stem}_{counter}{item.suffix}"
        while destination.exists():
            counter+=1
            destination=target_folder/f"{item.stem}_{counter}{item.suffix}"
        print("new available destination: ",destination)
        item.rename(destination)
for item in folder.iterdir():
    if not item.is_file():
        continue
    print("Checking file:", item.name)
    extension=item.suffix.lower()
    if extension in image_format:
        print("image")
        image_folder= folder / "Images"
        move_file(item, image_folder)
    elif extension==".pdf":
        print("document")
        document_folder= folder / "Document"
        move_file(item, document_folder)
    elif extension==".mp3":
        print("audio")
        audio_folder= folder / "Audio"
        move_file(item, audio_folder)
    else:
        print("unknown type of file")
