#FFT - sinal freq.domain (amplitudes) -> freqs extracted from FFT
#FFT_new - amps modified based on freqs
#Sig_out - ifft(FFT_new


import scipy.io.wavfile as wavfile
import scipy
import scipy.fftpack as fftpk
from scipy.io.wavfile import write
import numpy as np
from matplotlib import  pyplot as plt


rate, signal = wavfile.read('input.wav')

FFT = abs(scipy.fft(signal))
freqs = fftpk.fftfreq(len(FFT), (1.0 / rate))


#INTERVALLUMOKAT CSINALNI!   <------------------------  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#400000000 = 4

FFT_new = FFT.copy()
FFT_new[abs(freqs) < 5000] = 200000000 # 1800-ben felveszi 5


sig_out = fftpk.ifft(FFT_new)
write("output_new.wav", rate, sig_out.astype(signal.dtype))

#Testing
print('FFT values :', FFT)
print('FFT_new values :', FFT_new)
print('freqs values :', freqs)
print('Sig_out: ', sig_out)
plt.plot(freqs[range(len(FFT_new)//2)], FFT_new[range(len(FFT_new)//2)])
plt.xlabel("Frequency - Hz")
plt.ylabel("Amplitude")
plt.show()


#PROBAK

#for x in freqs:
#    if x < 0.05:
#        FFT_new = 4
#    else:
#        FFT_new = FFT

#freqs_new = freqs.copy()