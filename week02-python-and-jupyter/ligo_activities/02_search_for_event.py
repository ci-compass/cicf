# LIGO Data Analysis Activity 2: Finding an "Event"
#
# This script loads LIGO data and searches for the most
# interesting part of the data. Since we don't know if there is a
# real gravitational wave in this data, we will define "interesting"
# as the section with the highest variance (the "loudest" part).

import h5py
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Load the data file ---
data_file = '../H-H2_LOSC_4_V1-815235072-4096.hdf5'

try:
    data = h5py.File(data_file, 'r')
except IOError:
    print(f"Error: Could not open file {data_file}")
    exit()


# --- 2. Extract strain and metadata ---
strain = data['strain']['Strain'][()]
gps_start = data['meta']['GPSstart'][()]
dt = data['meta']['Duration'][()] / data['meta']['Detector'][()].size
num_samples = strain.shape[0]
time = np.arange(gps_start, gps_start + num_samples * dt, dt)


# --- 3. Search for the "loudest" chunk ---
# We will break the data into chunks and find the chunk
# with the highest variance.

chunk_size = 4096  # You can experiment with this value
num_chunks = num_samples // chunk_size

max_variance = 0
loudest_chunk_index = -1

print("Searching for the loudest chunk...")
for i in range(num_chunks):
    start = i * chunk_size
    end = start + chunk_size
    chunk = strain[start:end]
    variance = np.var(chunk)
    if variance > max_variance:
        max_variance = variance
        loudest_chunk_index = i

print(f"Loudest chunk found at index {loudest_chunk_index}")


# --- 4. Select the loudest chunk ---
start_index = loudest_chunk_index * chunk_size
end_index = start_index + chunk_size

loudest_time = time[start_index:end_index]
loudest_strain = strain[start_index:end_index]


# --- 5. Plot the loudest chunk ---
plt.figure(figsize=(12, 6))
plt.plot(loudest_time, loudest_strain)
plt.xlabel('Time (GPS seconds)')
plt.ylabel('Strain')
plt.title('Loudest Segment in LIGO Data')
plt.grid(True)


# --- 6. Save the plot ---
output_filename = 'event_plot.png'
plt.savefig(output_filename)
print(f"Plot of the loudest event saved as {output_filename}")


# --- 7. Close the file ---
data.close()
