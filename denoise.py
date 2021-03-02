import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [16, 12]
#plt.rcParams.update({'font.size', 10})

#signal with two frequencies
dt = 0.01
t = np.arange(0, 1, dt)
f = np.sin(2*np.pi*50*t) + np.sin(2*np.pi*120*t)
f_clean = f
f = f + 2.5*np.random.randn(len(t)) #noise

#FFT
n = len(t)
fhat = np.fft.fft(f, n)                         #fft
PSD = fhat * np.conj(fhat) / n                  #power spectrum(power/
freq = (1/(dt*n)) * np.arange(n)                #create x axis of freqs
L = np.arange(1, np.floor(n/2), dtype = 'int')  #only plot the first half

fig, axs = plt.subplots(2,1)

#use PSD to filter out noise
indices = PSD > 100         #Find freqs with large powers
PSDclean = PSD * indices    #Zero out all others
fhat = indices * fhat       #Zero out small Fourier coeffs in Y
ffilt = np.fft.ifft(fhat)   #Inverse FFT for filtered time signal

#PLOTS
plt.sca(axs[0])
plt.plot(t, f, color='c',LineWidth=1.5,label='Noisy')
plt.plot(t, f_clean, color='k',LineWidth=2,label='Clean')
plt.xlim(t[0],t[-1])
plt.legend()

plt.sca(axs[1])
plt.plot(t, ffilt, color='k',LineWidth=2,label='Filtered')
plt.xlim(t[0], t[-1])
plt.legend()

plt.sca(axs[2])
plt.plot(freq[L], PSD[L], color='c',LineWidth=2,label='Noisy')
plt.plot(freq[L], PSDclean[L], color='k',LineWidth=1.5,label='Filtered')
plt.xlim(freq[L[0]], freq[L[-1]])
plt.legend()

plt.show()