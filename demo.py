import scipy.io.wavfile as wavfile
import scipy
import scipy.fftpack as fftpk
import numpy as np
from matplotlib import  pyplot as plt


rate, signal = wavfile.read('input.wav')

FFT = abs(scipy.fft(signal))
freqs = fftpk.fftfreq(len(FFT), (1.0 / rate))

plt.plot(freqs[range(len(FFT)//2)], FFT[range(len(FFT)//2)])
plt.xlabel("Frequency - Hz")
plt.ylabel("Amplitude")
plt.show()

