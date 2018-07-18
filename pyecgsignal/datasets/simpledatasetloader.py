# import the necessary packages
import os
import numpy as np
import scipy.io
import scipy.signal as signal #import butter, lfilter, freqz
import math

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

        for matfile in [os.listdir(datamatPath)]:
            # load data from the matfile
            matData = scipy.io.loadmat(matfile)
            sampleContent = np.array(matData['M'])
            sampleRTime = np.array(matData['ATRTIME'])
            sampleTime = np.array(matData['TIME'])
            sampAnnote = np.array(matData['ANNOT'])
            matdata = sampleContent[:,1] #for we use only the first lead temporally
            filtdata = ecgfilter(matdata, frequency)
            normdata = ecgnorm(filtdata)

            sampleRTime = sampleRTime[3:len(sampleRTime)]
            rTime = round(frequency * sampleRTime)
            sampAnnote = sampAnnote[3:len(sampAnnote)]
            (frm_annot, filter_time) = annotfilt(sampAnnote, rTime) #remove the labels not used

            wave = []
            for (i, item) in filter_time:
                j = i + 1
                postime = filter_time[j+1] - filter_time[j]
                pretime = filter_time[j] - filter_time[j-1]

                if postime < 300 or pretime < 280:
                    tmp = adoptwind(filter_time(j), pretime, postime, normdata)
                else:
                    tmp = normdata[filter_time(j) - 140: filter_time(j) + 199, 1]

                wave.append(tmp)

        data.append(wave)
        labels.append(frm_annot[1:len(frm_annot)])
        return data

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



    def ecgnorm(self, data):

        mean = mean(data, 1)
        std = st


    def adoptwind(time, pretime, postime, normdata):

        wave = np.zeros(340)
        preselect = math.floor(pretime/2)
        postselect = math.floor(postime * 2/3)

        if preselect > 139: preselect = 139
        if postselect > 200: postselect = 200

        wave[(139 - preselect):(139 + postselect)] = normdata[(time - preselect - 1) : (time + postselect +1)]
        wave[0:(139 - preselect)] = wave[139 - preselect]
        wave[(139 + postselect):340] = wave[139 + postselect]



    def annotfilt(sampAnnote, sampleRTime):
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
        for (i, annot) in sampAnnote:
            if ~((annot <= 13) or (annot ==31) or (annot == 34) or (annot == 38)):
                deleteIndex.append(i)

        for (i, index) in deleteIndex:
            sampAnnote.pop(i)
            sampleRTime.pop(i)

        frm_annot = sampAnnote
        filter_time = sampleRTime

        return frm_annot, filter_time