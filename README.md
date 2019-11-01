# AugmentImagesAndXML

## Goal

The goal of this code is to to provide a easy to use and powerful data-augmenter which can be used to augment data (pictures and xml-files) for training object detection with machine learning, e.g. with Tensorflow(object detection).   
The Code is based on an [article](https://medium.com/@bhuwanbhattarai/image-data-augmentation-and-parsing-into-an-xml-file-in-pascal-voc-format-for-object-detection-4cca3d24b33b) which provides three code snippets for data augmentation.   
I connected these snippets so that it is much easier and comfortable to use.

## What it does

* creates 2 mirrowed pictures (horizontally + vertically)
* creates 3 rotated pictures
* creates 1 picture which colors are pca-distorted

This process is repeated twice with different color distortions

## How to use

1. Place your pictures in the "Pictures" folder and the corresponding xml-files in the "XML_Files_Input" folder
2. Run "AugmentPicturesMain" in Python (Python 3.8 not yet supported, use 3.7)
3. Wait...
4. The augmented data can be found in "AugmentedImages" and "AugmentedXML"

## Things that can be changed

If you don't want to have the solarize-option (reverses all PixelValues over threshold) change the Range of the for-loop in AugmentImageImagenetPolicy.py from 15 to 9.
