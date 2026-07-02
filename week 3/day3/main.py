from pathlib import Path

file_path = Path("text.txt") 

if file_path.is_file():
    print("The file exists!")
else:
    print("The file does not exist (or it is a folder).")
