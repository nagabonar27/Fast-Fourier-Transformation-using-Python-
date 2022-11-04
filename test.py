import sys
import matplotlib.pyplot as pl
import numpy as np
from scipy.fft import fft, fftfreq  #import module
from numpy.fft import fft, ifft

x = np.linspace(0, 10,  ) # create a location using linspace
y = np.sin(x)

print(x)
pl.figure(figsize = (8,6))
pl.plot(x,y)

samplingrate = 250 #hz
interval = 1/samplingrate
time = np.arange(0,1,interval)

f = 1

y = np.sin(2*np.pi*f*time)

pl.ylabel('amplitude')
pl.xlabel('time')
pl.plot(time,y)

yfft = fft(y) #calculate the fft of y
N = len(yfft)
n = np.arange(N)
T = N/samplingrate
freq = n/T

#plt.figure(figsize = (12, 6))

pl.subplot(121)
pl.xlabel('freq (Hz)')
pl.ylabel('FFT Amplitude |X(freq)|')
pl.stem(freq, np.abs(yfft), 'b', \
         markerfmt=" ", basefmt="-b")
pl.xlim(0,10)

pl.subplot(122)
pl.plot(time,y)
pl.xlabel('time')
pl.ylabel('amplitude')
pl.tight_layout

pl.show()