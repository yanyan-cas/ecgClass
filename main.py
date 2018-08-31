# Useage
# python for manifold learning -- ECG classification
import numpy as np
import matplotlib

from pyecgsignal.datasets.SimpleDataLoader import SimpleDataLoader

matplotlib.use('Agg')
import pyecgsignal
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
# from keras.preprocessing.image import img_to_array
# from keras.utils import np_utils
# from imutils import paths
import argparse
#import imutils
import os
from sklearn import manifold



# construct the argument parse and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-d", "--dataset", required = True, help = "path to input dataset of signals")
#args = vars(ap.parse_args())


# initialize the class labels
classLabels = ["Normal", "Supra-ventricular", "Ventricular", "Fusion"]

#signalPath = args["dataset"]
signalPath = "/Users/Yanyan/Documents/GITHUB/ecgClass/DATASET/MITBIH_Arrhythmia_MAT/"
# initial the list of data and labels
data = []
labels = []

# load the mat files
print("[INFO] loading ECG (sample) dataset...")
sdl = SimpleDataLoader()
frequency = 340
(data, labels) = sdl.loadMAT(signalPath, frequency)

# data augmentation
print("[INFO] performing data augmentation...")



# partition data sets
print("[INFO] partition the data into training and testing splits...")
# partition the data into training and testing splits using 80% of
# the data for training and the remaining 20% for testing
# (trainX, testX, trainY, testY) = train_test_split(data,
# 	labels, test_size=0.20, stratify=labels, random_state=42)


# pca































