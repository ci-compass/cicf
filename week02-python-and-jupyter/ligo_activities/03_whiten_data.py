# LIGO Data Analysis Activity 3: Whitening the Data
#
# This script loads LIGO data, finds the loudest chunk, and then
# "whitens" the data. Whitening is a process that helps to suppress
# background noise and make signals more visible.

import h5py
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch
from scipy.interpolate import interp1d

# --- 1. Load the data file and find the loudest chunk ---
# This part is the same as in the previous script.
data_file = '../H-H2_LOSC_4_V1-815235072-4096.hdf5'

try:
    data = h5py.File(data_file, 'r')
except IOError:
    print(f"Error: Could not open file {data_file}")
    exit()

strain = data['strain']['Strain'][()]
gps_start = data['meta']['GPSstart'][()]
dt = data['meta']['Duration'][()] / data['meta']['Detector'][()].size
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

# --- 2. Compute the Power Spectral Density (PSD) ---
# The PSD represents the noise spectrum of the data. We'll use Welch's
# method to estimate it.
fs = 1 / dt
freqs, psd = welch(strain, fs=fs, nperseg=chunk_size)

# We will need to interpolate the PSD to the same frequencies as the FFT of the data.
psd_interp = interp1d(freqs, psd)


# --- 3. Whiten the data ---
# Whitening involves dividing the Fourier transform of the data by the
# square root of the PSD.

# Take the Fourier transform of the loudest chunk
N = len(loudest_strain)
fft_data = np.fft.fft(loudest_strain)
fft_freqs = np.fft.fftfreq(N, dt)

# Whiten the data in the frequency domain
# We need to handle the zero frequency component carefully to avoid division by zero.
# We also only consider positive frequencies.
whitened_fft = np.zeros(N, dtype=complex)
for i in range(1, N // 2):
    if psd_interp(fft_freqs[i]) > 0:
        whitened_fft[i] = fft_data[i] / np.sqrt(psd_interp(fft_freqs[i]))
        whitened_fft[-i] = np.conj(whitened_fft[i]) # Ensure symmetry

# Take the inverse Fourier transform to get the whitened data in the time domain
whitened_strain = np.fft.ifft(whitened_fft)


# --- 4. Plot the original and whitened data ---
fig, axs = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

# Original data
axs[0].plot(loudest_time, loudest_strain)
axs[0].set_ylabel('Strain')
axs[0].set_title('Original Loudest Segment')
axs[0].grid(True)

# Whitened data
axs[1].plot(loudest_time, whitened_strain.real) # Plot the real part
axs[1].set_xlabel('Time (GPS seconds)')
axs[1].set_ylabel('Whitened Strain')
axs[1].set_title('Whitened Loudest Segment')
axs[1].grid(True)

plt.tight_layout()

# --- 5. Save the plot ---
output_filename = 'whitened_plot.png'
plt.savefig(output_filename)
print(f"Plot of whitened data saved as {output_filename}")


# --- 6. Close the file ---
data.close()
