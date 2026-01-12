# LIGO Data Analysis Activities

This directory contains a series of Python scripts to analyze LIGO data.
You should run them in order, from 01 to 04.

Each script builds on the previous one.

## How to run the scripts

First, make sure you have downloaded the data file. From the `week02-python-and-jupyter` directory, run:

```bash
wget https://gwosc.org/archive/data/S5/814743552/H-H2_LOSC_4_V1-815235072-4096.hdf5
```

Then, you can run each script from the `week02-python-and-jupyter/ligo_activities` directory.

### 1. Plot with time axis

This script will create a plot of the LIGO strain data with a proper time axis.

```bash
python 01_plot_with_time.py
```

It will save the plot as `plot_with_time.png`.

### 2. Search for the event

This script will find the event in the data and plot it.

```bash
python 02_search_for_event.py
```

It will save the plot as `event_plot.png`.

### 3. Whiten the data

This script will "whiten" the data to make the signal more visible.

```bash
python 03_whiten_data.py
```

It will save the plot as `whitened_plot.png`.

### 4. Plot a spectrogram

This script will create a spectrogram of the event, showing how the frequency of the signal changes with time.

```bash
python 04_plot_spectrogram.py
```

It will save the plot as `spectrogram.png`.
