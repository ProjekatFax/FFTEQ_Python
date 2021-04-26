import soundfile as sf
import matplotlib.pyplot as plt
import numpy as np


# Input the wave file
data , rate = sf.read("random_mono.wav")
length = data.shape[0]/rate
time = np.linspace(0,length,data.shape[0])

# Fourier transform
FFT_data = np.fft.rfft(data)

# Get the list of frequencies
freq = np.fft.rfftfreq(len(data), d=1./rate)

#Add plots
fig, axs = plt.subplots(2,2)
fig.suptitle('FFT filter')
fig.tight_layout(pad=3.0)


axs[0,0].plot(time, data)
axs[0,0].set_ylim([-1.1,1.1])
axs[0,0].title.set_text('original signal')
axs[0,0].set(xlabel="Time[s]", ylabel="Amplitude")

axs[0,1].plot(freq, FFT_data)
axs[0,1].title.set_text('original signal FFT')
axs[0,1].set(xlabel="Frequency[Hz]", ylabel="Amplitude")



#generate an array, 
#which contains the frequencies where the gaussian function will be generated
#it contains 10 elements
gauss_freq = [31,62,125,250,500,1000,2000,4000,8000,16000] 


#the amplitudes of the gaussian functions
amplitude_31 = 0
amplitude_62 = 0
amplitude_125 = 0
amplitude_250 = 0
amplitude_500 = 0
amplitude_1000 = 3
amplitude_2000 = 3
amplitude_4000 = 3
amplitude_8000 = 3
amplitude_16000 = 3 


#an array which contains the amplitudes of the gaussian functions 
amplitude =[amplitude_31,
            amplitude_62,
            amplitude_125,
            amplitude_250,
            amplitude_500,
            amplitude_1000,
            amplitude_2000,
            amplitude_4000,
            amplitude_8000,
            amplitude_16000]


#calculate the gaussian function
gaussian_function = 0
i = 0

while(i<10):
    gaussian_function += amplitude[i]* np.exp(-np.square(freq-gauss_freq[i])/(2*(gauss_freq[i]/3)**2))
    i = i+1


#apply gaussian filter
FFT_data += FFT_data  * gaussian_function


#normalize signal
normalize_value = np.max(amplitude)
FFT_data = FFT_data/normalize_value

# Convert back to time domain
newdata = np.fft.irfft(FFT_data)

# And save it to a new wave file
sf.write(file="test1.wav", data=newdata, samplerate=rate)

#plot the results
axs[1,0].plot(time, newdata)
axs[1,0].set_ylim([-1.1,1.1])
axs[1,0].title.set_text('filtered signal')
axs[1,0].set(xlabel="Time[s]", ylabel="Amplitude")


axs[1,1].plot(freq,FFT_data)
axs[1,1].title.set_text('filtered signal FFT')
axs[1,1].set(xlabel="Frequency[Hz]", ylabel="Amplitude")

plt.show()