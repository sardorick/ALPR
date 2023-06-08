# -*- coding: utf-8 -*-
"""Yolo.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MnqHOoaalClk4wuReJHaqfty0bFlO0-s
"""

import os
os.chdir('/content/drive/MyDrive/ANPR')

ls

!git clone https://github.com/ultralytics/yolov5

# Commented out IPython magic to ensure Python compatibility.
# %%bash
# cd yolov5
# pip install -r requirements.txt

os.chdir('yolov5')

ls

!python train.py --data data.yaml --cfg yolov5s.yaml --batch-size 8 --name Model --epochs 100

!python export.py --weights runs/train/Model/weights/best.pt --include torchscript onnx --simplify

