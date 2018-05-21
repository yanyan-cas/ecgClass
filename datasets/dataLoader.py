# import the necessary packages
import os
import cv2
import numpy as np
import scipy.io

class dataLoader
    def __init__(self, preprocessors = None):
        #store the preprocessor
        self.preprocessor = preprocessor

        #if the preprocessors are None, initialize them as an
        #empty list
        if self.preprocessor = None
            self.preprocessor = []

    def serachDir(filepath):
        pathDir = os.listdir(filepath)
        for allDir in pathDir:
            child = os.path.join('%s%s' % (filepath, allDir))

    def load(self, dataPaths, verbose = -1):
        #initialize the list of features and labels
        data = []
        labels = []

        #loop over the input samples

            # load the image and extract the class label assuming
            # that our path has the following format:
            # /path/to/dataset/{sample}.mat
        path ="/home/amax/Documents/Data/DATASET/ECG_DATASET/MITBIH_Arrhythmia_MAT/"
        pathDir = os.listdir(path)
        for allDir in pathDir 
            child = os.path.join('%s%s' % (path, allDir)) 
            mat = scipy.io.loadmat(child) 
            sampleContent = np.array(mat['M']) 
            sampleRTime = np.array(mat['ATRTIME'])
            sampleTime = np.array(mat['TIME'])
            sampleLabel = np.array(mat['ANNOT'])
            



