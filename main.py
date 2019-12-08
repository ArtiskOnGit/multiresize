from os import walk
from os.path import splitext
import os
from pathlib import Path
from PIL import Image


mypath = "./"

(_, _, filenames) = next(walk(mypath))

format = str(input("Format ? (.JPG,.png) >>>  "))
width = int(input("Width ? >>> "))
height = int(input("height ? >>> "))

if len(filenames) > 1 :
    for file in filenames :
        filename,ext = splitext(file)


        if ext == format:
            print(f"resizing : {file}")

            img = Image.open(file)
            img = img.resize((width,height))

            if not os.path.exists("./resized/"):
                os.makedirs("./resized/")

            path = Path("./resized/" + filename+ext)
            img.save(path)
        else:
            if ext != ".py":
                print(f"File with extension {ext} detected which does not correspond with {format}")
