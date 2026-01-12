# LIGO Data Analysis Activity 4: Plotting a Spectrogram
#
# This script creates a spectrogram of the loudest chunk of data.
# A spectrogram shows how the frequency content of a signal changes
# over time. This is a very useful tool for finding signals like
# gravitational waves, which have a characteristic "chirp" shape.

import h5py
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch
from scipy.interpolate import interp1d

# --- 1. Load the data and find the loudest chunk ---
data_file = '../H-H2_LOSC_4_V1-815235072-4096.hdf5'

try:
    data = h5py.File(data_file, 'r')
except IOError:
    print(f"Error: Could not open file {data_file}")
    exit()

strain = data['strain']['Strain'][()]
gps_start = data['meta']['GPSstart'][()]
dt = data['meta']['Duration'][()] / data['meta']['Detector'][()].size
fs = 1 / dt
num_samples = strain.shape[0]
time = np.arange(gps_start, gps_start + num_samples * dt, dt)

chunk_size = 4096
num_chunks = num_samples // chunk_size

max_variance = 0
loudest_chunk_index = -1

for i in range(num_chunks):
    start = i * chunk_size
    end = start + chunk_size
    chunk = strain[start:end]
    variance = np.var(chunk)
    if variance > max_variance:
        max_variance = variance
        loudest_chunk_index = i

start_index = loudest_chunk_index * chunk_size
end_index = start_index + chunk_size

loudest_time = time[start_index:end_index]
loudest_strain = strain[start_index:end_index]


# --- 2. Whiten the data ---
# We do this again to make the script self-contained.
freqs, psd = welch(strain, fs=fs, nperseg=chunk_size)
psd_interp = interp1d(freqs, psd)

N = len(loudest_strain)
fft_data = np.fft.fft(loudest_strain)
fft_freqs = np.fft.fftfreq(N, dt)

whitened_fft = np.zeros(N, dtype=complex)
for i in range(1, N // 2):
    if psd_interp(fft_freqs[i]) > 0:
        whitened_fft[i] = fft_data[i] / np.sqrt(psd_interp(fft_freqs[i]))
        whitened_fft[-i] = np.conj(whitened_fft[i])

whitened_strain = np.fft.ifft(whitened_fft).real


# --- 3. Create the spectrogram ---
plt.figure(figsize=(12, 6))

# The `specgram` function from matplotlib will create the spectrogram.
# NFFT is the number of data points used in each block for the FFT.
# A larger NFFT will give you more frequency resolution.
NFFT = 256
Pxx, freqs, bins, im = plt.specgram(whitened_strain, NFFT=NFFT, Fs=fs, noverlap=NFFT // 2)

plt.xlabel('Time (from start of chunk) (s)')
plt.ylabel('Frequency (Hz)')
plt.title('Spectrogram of Whitened Data')
plt.colorbar(label='Intensity (dB)')
plt.ylim(0, 500) # Limit frequency range to see details


# --- 4. Save the plot ---
output_filename = 'spectrogram.png'
plt.savefig(output_filename)
print(f"Spectrogram saved as {output_filename}")


# --- 5. Close the file ---
data.close()
