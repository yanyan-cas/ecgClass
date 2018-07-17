# Useage
# python for manifold learning -- ECG classification
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from keras.preprocessing.image import img_to_array
from keras.utils import np_utils
from imutils import paths
import argparse
import imutils
import os

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True, help = "path to input dataset of signals")
args = vars(ap.parse_args())


print("[INFO] loading ECG (sample) dataset...")




# initial the list of data and labels
data = []
labels = []

# loop over the original data














