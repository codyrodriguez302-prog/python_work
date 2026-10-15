from pathlib import Path
folder = Path.home() / "Downloads"
print(folder)
image_format={".jpg",".jpeg",".png",".gif",".webp",".bmp",
".tif",".tiff",".svg",".heic",".heif",".avif",".ico",".raw",".dng",".jfif",}
for item in folder.iterdir():
    if not item.is_file():
        continue
    print("Checking file:", item.name)
    extension=item.suffix.lower()
    if extension in image_format:
        print("image")
        image_folder= folder / "Images"
        image_folder.mkdir(exist_ok=True)
        destination= image_folder / item.name
        if not destination.exists():
            print("safe to move")
            item.rename(destination)
        else:
            print("file already exist")
        print(destination)
    elif extension==".pdf":
        print("document")
        document_folder= folder / "Document"
        document_folder.mkdir(exist_ok=True)
        destination= document_folder / item.name
        if not destination.exists():
            print("safe to move")
            item.rename(destination)
        else:
            print("file already exist")
    elif extension==".mp3":
        print("audio")
        audio_folder= folder / "Audio"
        audio_folder.mkdir(exist_ok=True)
        destination = audio_folder / item.name
        if not destination.exists():
            print("safe to move")
            item.rename(destination)
        else:
            print("file already exist")
    else:
        print("unknown type of file")

    