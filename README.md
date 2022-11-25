# Moving-Vehicle-Registration-Plate-Detection
Project for the Academia-Industry Conclave Hackathon 1.0 conducted at MIT Manipal. The method we used was to train a YOLOv5 model on our custom data set and optimize
the model using the OpenVINO framework for better performance on edge devices. The data set we used is available on https://www.kaggle.com/datasets/jayanthshanmugam/indian-vehicles-license-plate.
This repository contains only the final OpenVINO files that were converted from the YOLOv5 Pytorch files. To run inference, you can either use the detect.py provided in the 
YOLOv5 repository, or use the OpenVINO inference engine (much faster). 
Additionally, we also added the code for performing OCR on the number plates using the easyOCR engine. 
