import shutil
import os
import sys
from PIL import Image

# shutil.copy("house.csv", "house_copy.csv")

# os.remove("house.csv")
# os.rename("house_copy.csv", "house1.csv")
# os.replace("house1.csv", "house.csv")

# images = ["image1.png", "image2.png", "image3.png"]
# for img in images:
#     with Image.open(img) as image:
#         image.save(f"copy_{img}")


# shutil.copytree("images", "images_dir")

#Copy folders safely
src = "images"
dst = "images_dir"

if not os.path.exists(dst):
    shutil.copytree(src, dst)

#We can still deliberately override folders
shutil.copytree("images", "images_dir", dirs_exist_ok=True)
#This merges into the existing folder — files with the same name get overwritten.

