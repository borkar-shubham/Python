#os.path.exists()
import os

file1_path = "./file1.txt"

if os.path.exists(file1_path):
    print("File exists")
else:
    print("File does not exists")

#pathlib.Path.exists()
from pathlib import Path

file2_path = Path("./abc123.txt")

if file2_path.exists():
    print("File exists.")
else:
    print("File does not exists, creating new file..!")
    fh = open(file2_path, 'xt')
    fh.write("Creating a file and adding the contents in it.")
    fh.close()