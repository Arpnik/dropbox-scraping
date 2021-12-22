import img2pdf
import os, cv2
import PIL

from com.scrappy.PropertyConfig import getFolderPath


def getImages(folder_loc):
    images = []
    for file in os.listdir(folder_loc):
        img = cv2.imread(os.path.join(folder_loc, file))
        if img is not None:
            images.append(img)
    return images


def generatePdfFromPictures():
    folder_loc = getFolderPath()
    files = [os.path.join(folder_loc, i) for i in os.listdir(folder_loc) if i.endswith(".jpg")]
    files.sort(key=os.path.getmtime)
    print(files)
    images = [PIL.Image.open(i) for i in files]
    with open(os.path.join(folder_loc, "output.pdf"), "wb") as f:
        f.write(img2pdf.convert([i.filename for i in images]))
