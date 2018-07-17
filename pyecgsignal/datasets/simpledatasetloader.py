# import the necessary packages
import os
import cv2
import numpy as np
import scipy.io
import scipy.signal as signal #import butter, lfilter, freqz

class SimpleDataLoader
    def __init__(self, preprocessors = None):
        #store the preprocessor
        self.preprocessor = preprocessor

        #if the preprocessors are None, initialize them as an
        #empty list
        if self.preprocessor = None
            self.preprocessor = []

    #def serachDir(self, filepath):
    #    pathDir = os.listdir(filepath)
    #    for allDir in pathDir:
    #        child = os.path.join('%s%s' % (filepath, allDir))

    def loadMAT(self, datamatPath, frequency, verbose = -1):

        #initialize the list of features and labels
        data = []
        labels = []

        #loop over the input samples

            # load the image and extract the class label assuming
            # that our path has the following format:
            # /path/to/dataset/{sample}.mat
        #path ="/home/amax/Documents/Data/DATASET/ECG_DATASET/MITBIH_Arrhythmia_MAT/"
        pathDir = os.listdir(datamatPath)

        for matfile in [os.listdir(datamatPath)]
            # load data from the matfile
            matData = scipy.io.loadmat(matfile)
            sampleContent = np.array(matData['M'])
            sampleRTime = np.array(matData['ATRTIME'])
            sampleTime = np.array(matData['TIME'])
            sampAnnote = np.array(matData['ANNOT'])
            mat = matData[:,1] #for we use only the first lead temporally
            mat = ecgFilter(mat, frequency)
            mat = ecgNorm(mat)

            rTime = round(frequency * sampleRTime(4:size(sampleRTime,1)-1,1))
            annot = ecgAnnoteSample(4:size(sampAnnote,1)-1,1)
            (frm_annot, filter_time) = myAnnoteFilter(annot, Rtime) #remove the labels not used

            for j = 2: size(filter_time, 1) - 1 # split data into windows
                tmp = zeros(340, 1);
                pos_time = filter_time(j + 1) - filter_time(j)
                pre_time = filter_time(j) - filter_time(j - 1)

                if pos_time < 300 || pre_time < 280
                    tmp = adaptWind(filter_time(j), pre_time, pos_time, norm_data)
                else
                    tmp = norm_data(filter_time(j) - 140: filter_time(j) + 199, 1)

                wave.append(tmp)
            end

            wdata.append(wave)
            labels.append( frm_annot(2:end - 1)')
            
    return


    def ecgNorm(self, ):
        self.preprocessor


    def ecgAnnoteSample(self, ):
        self.preprocessor

    def ecgAnnoteFilter():
        self.preprocessor


    def ecgFilter(self, data, frequency)
        # using the scipy package to design signal filters
        # using the Butterworth filter
        wp = 1 * 2 / frequency
        ws = 0.1 * 2 / frequency
        gpass = 3
        gstop = 45
        N, Wn = signal.buttord(wp, ws, gpass, gstop, False)
        b, a = signal.butter(N, Wn, 'high', False, 'ba')
        w, h = signal.filtfilt(b, a, data)
        return w



