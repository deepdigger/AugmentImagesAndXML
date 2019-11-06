from autoaugment import ImageNetPolicy
from PIL import Image
import glob
import xml.etree.ElementTree as ET
import StaticMethods as sm
print("opened")
sm.createFolder("AutoAugmentImages")
sm.createFolder("AutoAugmentXML")
policy = ImageNetPolicy()

for XMLPath in glob.glob("XML_Files_Input/*"):
    print(XMLPath)
    fileName = XMLPath.split("/")[1].split(".")[0]
    SplitAtDotXMLPath = XMLPath.split(".")
    tree = ET.parse(XMLPath)
    tree.write("AutoAugmentXML/" + fileName + ".xml")
    root = tree.getroot()
    try:
        print("Pictures/" + fileName + ".jpg")
        img = Image.open("Pictures/" + fileName + ".jpg")
        img.save("AutoAugmentImages/" + fileName + ".jpg")


        print("Autoaugment: %s" % root.find("filename").text)
        for i in range(15):
            newName = fileName + "AutoAugment" + str(i)
            root.find("filename").text = newName + ".jpg"
            tree.write("AutoAugmentXML/" + newName + ".xml")
            augmentedImage = policy(img, i)
            augmentedImage.save("AutoAugmentImages/" + newName + ".jpg")

    except FileNotFoundError:
        print("Image: %s not found" % fileName)
