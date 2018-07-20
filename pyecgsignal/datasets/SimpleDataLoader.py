# import the necessary packages
import os
import numpy as np
import scipy.io
import scipy.signal as signal #import butter, lfilter, freqz
import math
from sklearn.preprocessing import normalize


class SimpleDataLoader:
    def __init__(self, preprocessor = None):
        #store the preprocessor
        self.preprocessor = preprocessor

        #if the preprocessors are None, initialize them as an
        #empty list
        if self.preprocessor == None:
            self.preprocessor = []

    def loadMAT(self, datamatPath, frequency):
        #initialize the list of features and labels
        data = []
        labels = []
        files = os.listdir(datamatPath)
        files.sort()

        print ('loadMAT',datamatPath, files)
        #loop over the input data files from the directory
        count = 0
        for matfile in files:
            if matfile.__contains__('DS'):
                continue
            # load mat file from the folder
            print('loadMAT', matfile)
            file = datamatPath + matfile
            matData = scipy.io.loadmat(file)
            sampleContent = np.array(matData['M'])
            sampleRTime = np.array(matData['ATRTIME'])
            sampleTime = np.array(matData['TIME'])
            sampAnnote = np.array(matData['ANNOT'])

            # decide the channels used in the experiments
            matdata = sampleContent[:,1] # for we use only the first lead temporally

            # digital filtering of signals
            filtdata = self.ecgfilter(matdata, frequency)

            # signal pre-processing of normalization
            # normdata = self.ecgnormalize(filtdata)

            # time series segmentation: separate the samples from continuous time series
            sampleRTime = sampleRTime[3:len(sampleRTime)]
            rTime = np.round(frequency * sampleRTime) # using the R-wave positions
            sampAnnote = sampAnnote[3:len(sampAnnote)]
            (frm_annot, filter_time) = self.annotfilt(sampAnnote, rTime) # remove the labels not used

            # loop over the single mat file in the directory
            wave = []
            j = 0
            for item in filter_time:
                j = j + 1

                # determine the signal duration
                postime = filter_time[j+1] - filter_time[j]
                pretime = filter_time[j] - filter_time[j-1]

                if postime < 300 or pretime < 280:
                    tmp = self.adoptwind(filter_time[j], pretime, postime, filtdata)
                else:
                    tmp = filtdata[filter_time[j] - 140: filter_time[j] + 199, 1]
                # data samples from one single mat file
                wave.append(tmp)
                # output info for data loading
            count += 1
            print("[INFO] loading ECG dataset, file num = {}".format(count))

        # Append all the sample from a single file, to build the whole data set
        data.append(wave)
        labels.append(frm_annot[1:len(frm_annot)])

        # return the whole data set
        return (data, labels)

    def ecgfilter(self, data, frequency):
        # using the scipy package to design signal filters
        # using the ButterWorth filter
        wp = 1 * 2 / frequency
        ws = 0.1 * 2 / frequency
        gpass = 3
        gstop = 45
        (N, Wn) = signal.buttord(wp, ws, gpass, gstop, False)
        (B, A) = signal.butter(N, Wn, 'high')
        w = signal.filtfilt(B, A, data)
        # return the output
        return  w

    def adoptwind(self, time, pretime, postime, normdata):
        # each sample with 340 points
        wave = np.zeros(340)
        preselect = math.floor(pretime/2)
        postselect = math.floor(postime * 2/3)
        if preselect > 139: preselect = 139
        if postselect > 200: postselect = 200
        wave[(139 - preselect):(139 + postselect)] = normdata[(time - preselect - 1) : (time + postselect +1)]
        wave[0:(139 - preselect)] = wave[139 - preselect]
        wave[(139 + postselect):340] = wave[139 + postselect]

        return wave

    def annotfilt(self, sampAnnote, sampleRTime):
        # % We now just care about the annotations below 17,so we filter the annotations beyond 16
        # Mapping of MIT-BIH arrhythmia database heartbeat types to the AAMI heartbeat classes:
        # on-ectopic beats(N),Supra-ventricular ectopic beats(S),Ventricular ectopic
        # beats(V),Fusion beats(F),Unknown beats(Q)
        # AAMI heartbeat classes MIT-BIH heartbeat classes labels
        # N NORMAL / * normal beat * / 1
        # N LBBB/* left bundle branch block beat */             2
        # N RBBB/* right bundle branch block beat */            3
        # N NESC/* nodal (junctional) escape beat */            11
        # N AESC/* atrial escape beat */                      34
        # S ABERR/* aberrated atrial premature beat */          4
        # S NPC/* nodal (junctional) premature beat */          7
        # S APC/* atrial premature contraction */               8
        # S SVPB/* premature or ectopic supraventricular beat*/   9
        # V VESC/* ventricular escape beat */                  10
        # V PVC/* premature ventricular contraction */           5
        # V FLWAV/* ventricular flutter wave */                 31
        # F FUSION/* fusion of ventricular and normal beat */     6
        # Q PACE/* paced beat */                              12
        # Q UNKNOWN/* unclassifiable beat */                    13
        # Q PFUS/* fusion of paced and normal beat */            38

        # Ac_index = find [annot <= 13 or annot ==31 or annot == 34 or annot == 38]

        deleteIndex = []
        count = -1
        for annot in sampAnnote:
            count = count + 1
            if ~((annot <= 13) or (annot ==31) or (annot == 34) or (annot == 38)):
                deleteIndex.append(count)

        for index in deleteIndex:
            sampAnnote.pop(index)
            sampleRTime.pop(index)

        frm_annot = sampAnnote
        filter_time = sampleRTime

        return (frm_annot, filter_time)

    def ecgnormalize(self, data):
    #    normalize
    #    mean = mean(data, 1)
    #    std = 5 * std(data, 0, 1)
        normalize
