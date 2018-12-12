#from pylab import*
import matplotlib.pyplot as plt
from scipy.io import wavfile
import numpy as np
import wave

def plot_wave(file,color,linewidth):
	with wave.open(file,'r') as wav_file:
		fs = wav_file.getframerate()  #44100hz
		fr = wav_file.getnframes()
		
		
		signal = wav_file.readframes(-1)
		signal = np.frombuffer(signal, 'int16')
				
		s2 = signal[::2] #every other element, in this case, 1 channel of sterio
		#s3 = signal[1::2] #get the other channel
		#s2 = s2/(2.**15) #adjust the data to float (-1<s2<1)
	
		timeArray = np.arange(0, fr, 1)
		timeArray = timeArray/fs
		timeArray = timeArray * 1000
		
		#plt.figure()
		# plt.title('Signal Wave...')
		# plt.ylabel('Amplitude')
		# plt.xlabel('Time (ms)')
		plt.plot(timeArray,s2,color,linewidth)
		#plt.plot(timeArray,s3)
		#plt.show()
	



