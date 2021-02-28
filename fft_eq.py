#  https://www.dummies.com/programming/python/performing-a-fast-fourier-transform-fft-on-a-sound-file/
#  https://github.com/Jayu8/Audio-Equalizer-/commit/72afa51d70ec6f6acdd5172324cda46909d1cc04  -- GUI --
#  https://mizzlrblog.wordpress.com/2016/06/18/fun-with-fft-lets-build-an-equalizer-in-matlab/?fbclid=IwAR3yCPsS09e1iiGL6Zt4KFFKxhqO7SJYCjdLwyG-cIitruE0RVLe6th4kow  -- MATLAB EQ --
#  https://dsp.stackexchange.com/questions/41368/applying-a-filter-on-an-audio-signal-with-python


import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fft import fft
import numpy as np
#import struct
from scipy.io.wavfile import write

#audio = []
#sample_rate = 44100.0

rate, data = wav.read('input.wav')

fft_out = fft(data)

#-------------------------------------------------------------------------------------
##### make new wav file #####  EZ NEM KELL,
#def save_wav(file_name):
#   Open up a wav file
#    wav_file=wav.open(file_name)

#    # wav params
#    nchannels = 1

#    sampwidth = 2

    # 44100 is the industry standard sample rate - CD quality.  If you need to
    # save on file size you can adjust it downwards. The stanard for low quality
    # is 8000 or 8kHz.
#    nframes = len(audio)
#    comptype = "NONE"
#    compname = "not compressed"
#    wav_file.setparams((nchannels, sampwidth, sample_rate, nframes, comptype, compname))

    # WAV files here are using short, 16 bit, signed integers for the
    # sample size.  So we multiply the floating point data we have by 32767, the
    # maximum value for a short integer.  NOTE: It is theortically possible to
    # use the floating point -1.0 to 1.0 data directly in a WAV file but not
    # obvious how to do that using the wave module in python.
#    for sample in audio:
#        wav_file.writeframes(struct.pack('h', int( sample * 32767.0 )))

#    wav_file.close()
#    return
#save_wav("output.wav")
#------------------------------------------------------------------------

###### filtered---------CSAK EGY PROBA-------------------------------------------------
#filtered = low_pass_filter(data)
#-----------------------------------------------------------------------

# EQ---------------------bandpasst meg kell csinalni--------------------------------------------------
#def equalizer_10band (data, fs, gain1=0, gain2=0, gain3=0):
#    band1 = bandpass_filter(data, 20, 39, fs, order=2)* 10**(gain1/20)
#    band2 = bandpass_filter(data, 40, 79, fs, order=3)*10**(gain2/20)
#    band3 = bandpass_filter(data, 80, 159, fs, order=3)*10**(gain3/20)


#-------------------------------------------------------------------------


write("output.wav", rate, data)

plt.plot(data, np.abs(fft_out))
plt.show()