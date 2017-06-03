from scipy.signal import butter, lfilter

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.signal import freqz
    import soundfile as sf

    # Read input wav file
    data, fs = sf.read('david1.wav')

    Time0 = np.linspace(0, len(data)/fs, num=len(data))

    # Sample rate and desired cutoff frequencies (in Hz).
    lowcut = 70.0
    highcut = 2000.0

    #apply bandpass filter
    y = butter_bandpass_filter(data, lowcut, highcut, fs, order=6)

    #output filtered wav file 
    sf.write('entry.wav', y, fs)
