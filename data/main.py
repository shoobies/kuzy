import wav_utility as wu
import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np
import wave



plt.figure()
#plt.axis([0,300000, 0, 1000])		this needs to be setup so the plot screen isnt blank
wu.plot_wave('outside.tl.wav', 'b', 1)

wu.plot_wave('outsidetest.np.wav','r', 2)



#wu.plot_wave('outsidetest.tp.wav','r', 1) , not working 
plt.show()