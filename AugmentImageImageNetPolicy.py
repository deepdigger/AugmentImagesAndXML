from autoaugment import ImageNetPolicy
from PIL import Image
import glob
import xml.etree.ElementTree as ET


policy = ImageNetPolicy()

for image in glob.glob("Pictures\\*"):
    img = Image.open(image)
    imageSplitNameDot = image.split(".")
    fileName = image.split("\\")[1].split(".")[0]
    tree = ET.parse("XML_Files_Input\\" + fileName + ".xml")
    root = tree.getroot()
    print(str(root.find("filename").text))
    for i in range(15):
        newName = fileName + "AutoAugment" + str(i)
        root.find("filename").text = newName + ".jpg"
        tree.write("XML_Files_Input\\" + newName + ".xml")
        augmentedImage = policy(img, i)
        augmentedImage.save("Pictures\\" + newName + ".jpg")


#imgs[0].save("Pictures/augmented.jpg")