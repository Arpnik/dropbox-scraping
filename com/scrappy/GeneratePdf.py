import img2pdf
import os, cv2
import PIL

from com.scrappy import EXTENSION
from com.scrappy.PropertyConfig import getFolderPath


def getImages(folder_loc):
    images = []
    for file in os.listdir(folder_loc):
        img = cv2.imread(os.path.join(folder_loc, file))
        if img is not None:
            images.append(img)
    return images


def generatePdfFromPictures():
    folderLoc = getFolderPath()
    files = [os.path.join(folderLoc, i) for i in os.listdir(folderLoc) if i.endswith(EXTENSION)]
    files.sort(key=os.path.getmtime)
    # print(files)
    images = [PIL.Image.open(i) for i in files]
    with open(os.path.join(folderLoc, "output.pdf"), "wb") as f:
        f.write(img2pdf.convert([i.filename for i in images]))
    [i.close() for i in images]
    deleteImages(folderLoc)


def deleteImages(folderLoc):
    for file in os.listdir(folderLoc):
        if file.endswith(EXTENSION):
            os.remove(os.path.join(folderLoc, file))