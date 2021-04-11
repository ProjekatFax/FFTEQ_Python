import scipy.io.wavfile
import soundfile as sf

import numpy as np
from matplotlib import  pyplot as plt


# Input the wave file
data , rate = sf.read("input.wav")
length = data.shape[0]/rate
time = np.linspace(0,length,data.shape[0])

# Fourier transform
FFT_data = np.fft.rfft(data)

# Get the list of frequencies
freq = np.fft.rfftfreq(len(data), d=1./rate)

# Find the bin closest to 1kHz and attenuate
#idx = (np.abs(freq - 1.E3)).argmin()
#FFT_data[idx] *= 1./2

# Find the bin closest to 440 Hz and set a continuous tone
#idx = (np.abs(freq - 440)).argmin()
#FFT_data[idx] = max( abs( FFT_data) )

#Pazi sad
idx = (np.abs(freq - 10.E3)).argmin()
FFT_data[idx] = max(abs(FFT_data))


# Add a Gaussian pulse, width in frequency is inverse of its duration
#FFT_data += max( abs( FFT_data) )/2. * np.exp( -((freq-880)/5.)**2freq )

# Convert back to time domain
newdata = np.fft.irfft(FFT_data)

# And save it to a new wave file


fig, axs = plt.subplots(2)
axs[0].plot(time, data)
axs[1].plot(time, newdata)

plt.show()


sf.write(file="test_out.wav", data=newdata, samplerate=rate)
