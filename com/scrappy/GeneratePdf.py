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

#TODO sort the files on date and than form pdf
def generatePdfFromPictures():
    folder_loc = getFolderPath()
    files = os.listdir(folder_loc)
    images = [PIL.Image.open(os.path.join(folder_loc, i)) for i in files if i.endswith(".jpg")]
    with open(os.path.join(folder_loc, "output.pdf"), "wb") as f:
        f.write(img2pdf.convert([i.filename for i in images]));
