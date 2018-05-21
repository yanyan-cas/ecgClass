#This file is for pre-processing 
import scipy.signal import butter, lfilter, freqz
class preprocessor:
    def __init__(self, sampleRate):
        self.sampleRate = sampleRate

    
    def dataFilter(data, frequency)
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


    def normalize()
        

    def preprocess(self, data)
        mat = data  
        sampleContent = np.array(mat['M'])
        sampleRTime = np.array(mat['ATRTIME'])
        sampleTime = np.array(mat['TIME'])
        sampleLabel = np.array(mat['ANNOT'])
       
       for singleBeat in sampleContent
            
            filtBeat = dataFilter(singleBeat[1], sampleRate)
            normBeat = normalize(filtBeat)
            rTime = 
            beatAnnote = 
            []
            
        return data
