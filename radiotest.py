# must have pkg-config and libusb
# and pyrtlsdr
# https://witestlab.poly.edu/blog/capture-and-decode-fm-radio/

from rtlsdr import RtlSdr
from rtlsdr import RtlSdrTcpClient
import numpy as np
import scipy.signal as signal
import sounddevice as sd
import scipy.io.wavfile as writer

def main():
	sdr = RtlSdr()
	sdr.sample_rate = 3.2e6 #2.048e6
	sdr.center_freq = 100100000 #70e6
	sdr.freq_correction = 60
	sdr.gain = 'auto'
	samples = sdr.read_samples(4096)
	print(samples, type(samples))
	demod_list = []
	for ind in range(len(samples)-1):
		demod_list.append(np.angle(np.conj(samples[ind]) * samples[ind+1]))

	writer.write('sample.wav', 200000, np.array(demod_list))
	
	# client = RtlSdrTcpClient(hostname='192.168.1.100', port=12345)
	# client.center_freq = 100100000
	# data = client.read_samples()
	# print(data)

def resampleAndPlayAudio(input):
    #orginal samples where taken at 200kHZ need to down sample to 44.1kHz
    #keep every 4 sample  200kHz /44.1kHz = 4.5
    result = input[::4]
    # plt.plot(result)
    sd.play(result,44100)
	

if __name__ == "__main__":
    main()