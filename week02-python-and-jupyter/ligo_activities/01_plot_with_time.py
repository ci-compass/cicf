# LIGO Data Analysis Activity 1: Plotting with a time axis
#
# This script loads LIGO data from an HDF5 file, creates a time axis,
# and plots the strain data over time.

import h5py
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Load the data file ---
# The data file is expected to be in the parent directory.
# If it's not, you can change the path here.
data_file = '../H-H2_LOSC_4_V1-815235072-4096.hdf5'

try:
    data = h5py.File(data_file, 'r')
except IOError:
    print(f"Error: Could not open file {data_file}")
    print("Please make sure you have downloaded the data file and it is in the correct directory.")
    exit()

# --- 2. Explore the data ---
# You can uncomment these lines to see the structure of the file
# print("Keys in the HDF5 file:")
# for key in data.keys():
#     print(key)

# print("\nMetadata:")
# for key, value in data['meta'].items():
#     print(f"  {key}: {value[()]}")


# --- 3. Extract strain and metadata ---
# The strain data is what we are interested in.
strain = data['strain']['Strain'][()]

# We also need some metadata to create the time axis.
# GPS start time of the data
gps_start = data['meta']['GPSstart'][()]
# The time step between data points
dt = data['meta']['Duration'][()] / data['meta']['Detector'][()].size


# --- 4. Create the time axis ---
# The number of data points
num_samples = strain.shape[0]

# Create a time array starting from the GPS start time
# and with a step of dt.
time = np.arange(gps_start, gps_start + num_samples * dt, dt)

# The time array and strain array should have the same length.
# It's a good practice to check this.
# print(f"Length of time array: {len(time)}")
# print(f"Length of strain array: {len(strain)}")


# --- 5. Plot the data ---
# Now we can plot the strain data against the time axis.
# We will only plot the first 10,000 points to see the details.
num_points_to_plot = 10000

plt.figure(figsize=(12, 6))
plt.plot(time[:num_points_to_plot], strain[:num_points_to_plot])
plt.xlabel('Time (GPS seconds)')
plt.ylabel('Strain')
plt.title('LIGO Strain Data')
plt.grid(True)


# --- 6. Save the plot ---
# Save the plot to a file.
output_filename = 'plot_with_time.png'
plt.savefig(output_filename)
print(f"Plot saved as {output_filename}")

# You can also show the plot directly if you are running this interactively.
# plt.show()

# --- 7. Close the file ---
data.close()
