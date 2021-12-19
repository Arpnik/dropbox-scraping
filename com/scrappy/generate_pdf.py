import img2pdf
import os, cv2
import PIL

from com.scrappy.property_config import get_folder_path


def get_images(folder_loc):
    images = []
    for file in os.listdir(folder_loc):
        img = cv2.imread(os.path.join(folder_loc, file))
        if img is not None:
            images.append(img)
    return images


def generate_pdf_from_pictures():
    folder_loc = get_folder_path();
    images = [PIL.Image.open(os.path.join(folder_loc, i)) for i in os.listdir(folder_loc) if i.endswith(".jpg")]
    with open(os.path.join(folder_loc, "output.pdf"), "wb") as f:
        f.write(img2pdf.convert([i.filename for i in images]));
