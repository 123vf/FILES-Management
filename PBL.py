import os
import shutil
#os.chdir("D://")
#print(os.getcwd())
path = r"D:\pbl"
files = os.listdir(path)

for items in files:
    #print(f"file name is {items} and the extension is {items.split('.')[1]}")
    #print(items)
    a = items.split('.')[1]
    if a == "bmp":
        if os.path.exists("D:/pbl/images"):
            shutil.move("D:/pbl/"+items, "D:/pbl/images")
        else:
            os.mkdir("D:/pbl/images")
            shutil.move("D:/pbl/"+items, "D:/pbl/images")
    elif a == "xlsx":
        if os.path.exists("D:/pbl/excel"):
            shutil.move("D:/pbl/"+items, "D:/pbl/excel")
        else:
            os.mkdir("D:/pbl/excel")
            shutil.move("D:/pbl/"+items, "D:/pbl/excel")
    elif a == "txt":
        if os.path.exists("D:/pbl/documents"):
            shutil.move("D:/pbl/"+items, "D:/pbl/documents")
        else:
            os.mkdir("D:/pbl/documents")
            shutil.move("D:/pbl/"+items, "D:/pbl/documents")
    elif a == "accdb":
        if os.path.exists("D:/pbl/office"):
            shutil.move("D:/pbl/"+items, "D:/pbl/office")
        else:
            os.mkdir("D:/pbl/office")
            shutil.move("D:/pbl/"+items, "D:/pbl/office")
    elif a == "pptx":
        if os.path.exists("D:/pbl/powerpoint presentation"):
            shutil.move("D:/pbl/"+items, "D:/pbl/powerpoint presentation")
        else:
            os.mkdir("D:/pbl/powerpoint presentation")
            shutil.move("D:/pbl/"+items, "D:/pbl/powerpoint presentation")
    elif a == "pub":
        if os.path.exists("D:/pbl/publisher document"):
            shutil.move("D:/pbl/"+items, "D:/pbl/publisher document")
        else:
            os.mkdir("D:/pbl/publisher document")
            shutil.move("D:/pbl/"+items, "D:/pbl/publisher document")
    elif a == "docx":
        if os.path.exists("D:/pbl/word documents"):
            shutil.move("D:/pbl/"+items, "D:/pbl/word documents")
        else:
            os.mkdir("D:/pbl/word documents")
            shutil.move("D:/pbl/"+items, "D:/pbl/word documents")

