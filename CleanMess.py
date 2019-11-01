import os
import shutil

filesToRemove = ["AugmentedXmlDataPath.txt",
                 "file_name.txt",
                 "converted_annotation_in_txt",
                 "AutoAugmentImages",
                 "AutoAugmentXml"]
for file in filesToRemove:
    try:
        os.remove(file)
    except PermissionError:
        shutil.rmtree(file)
    except FileNotFoundError:
        print("File or path: %s not found" % file)

print("Removing finished")