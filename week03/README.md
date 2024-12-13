# CICF Week 3

The goals for week 3 lab are:

1. Install and use the Jupyter notebook application on your VM.
2. Be able to create, edit, and run notebooks.
3. Use the NumPy and MatPlotLib packages.
4. Download data from LIGO and know what an HDF5 file is.


## Tutorial

We need to install a couple of Debian packages on our VMs, using the
[apt] package manager:

```console
sudo apt install python3-pip wget
```

Type `Y` to confirm installation.

We also need some Python packages. These we can install using [pip]:

```console
pip install jupyter numpy scipy matplotlib h5py
```

[apt]: https://wiki.debian.org/AptCLI
[pip]: https://pip.pypa.io/en/stable/

Once we have installed what we need, let us download a dataset.  We
will need this later.

```console
cd cicf/week03
wget https://gwosc.org/archive/data/S5/814743552/H-H2_LOSC_4_V1-815235072-4096.hdf5
```

And then start Jupyter with the command below:

```console
jupyter notebook
```

You will see a browser window open displaying your filesystem.
Navigate to `cicf/week03/introduction.ipynb` and open it.

A Jupyter notebook consists of a bunch of _cells_ which contain either
text (in [Markdown] format), or python code and its output.

[Markdown]: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

The python code is _runnable_, which means you can select a python
cell and then choose the menu option "Cell > Run Cells".  Try running
both of the python cells in the notebook.

Commands to try:

```python
56
```

This produces an output. Notice the python input and output cells are
numbered in the order that they are run.

```python
56+7
```

The python cells will evaluate the expression and return its value

```python
print("hello")
```

Note that `print()` is an expression that outputs something the the
screen and then return the value `None`.

```python
import math

2*math.PI*5
```

The last command has an error. We can fix it and rerun the cell. It
should be `2*math.pi*5`.

### NumPy

The `math` library is part of the Python standard library.

It implements a routines to calculate few standard functions and some
basic probability distributions.

As noted in the lecture Python does not have an efficient built-in
array data type (rather, it approximates arrays by using lists and
nested lists).

The NumPy library implements an efficient array datatype, and is used
as a foundation for almost all scientific Python software.

```python
import numpy as np
```

The critical NumPy data type is the array.

"NumPy arrays are faster and more compact than Python lists. An array
consumes less memory and is convenient to use."
([source](https://numpy.org/doc/stable/user/absolute_beginners.html))
The one caveat with NumPy arrays is that all the elements inside an
array need to have the same data type (e.g. integer, float, double).

```python
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
```

The `array()` function will turn nested lists into an array.
You can also make new arrays by asking for a zero array of a given size

```python
z = np.zeros(3)
z
```

or ones:

```python
m = np.ones((3,3))
```

(note that the dimensions are given as a _tuple_).
You can get the dimensions of an array with the `.shape()` method:

```python
m.shape()
z.shape()
```

You can also element-wise add, subtract, or multiply:

```python
z + 3
```

Or

```python
a % 2
```

Comparisons are element wise

```python
a > 5
```

### NumPy Linear Algebra

NumPy has routines to do basic linear algebra, such as finding a
matrix inverse, or solving a linear system.

```python
k = np.array([1,1,1], [1,1,0], [1,0,0])
k
```

Inverses

```python
from numpy.linalg import nl
kinv = nl.inv(k)
kinv
```

And matrix multiplication

```python
k @ kinv
```

Matrix visualization:

```python
import matplotlib.pyplot as plt
plt.matshow(a)
```

### Working with LIGO Data

Lets plot some data from the LIGO observatory.
This dataset is in a binary format called HDF5.

```python
import h5py
dataFile = h5py.File('814743552/H-H2_LOSC_4_V1-815235072-4096.hdf5/', 'r')
```

We can look at the dataset:

```python
for k in dataFile.keys():
    print(k)
```

And

```python
for k,v in dataFile['meta'].items():
    print(k,v)
```

That is not quite what we want:

```python
for k,v in dataFile['meta'].items():
    print(k,v[...])
```

Lets load some of the data into an array.

```python
strain = dataFile['strain']['Strain']
N = 5000
plt.plot(range(N), strain[:N])
```

## Resources

Parts of this tutorial were taken from the [LIGO data tutorial](https://gwosc.org/tutorial02/).

- [Jupyter Manual](https://docs.jupyter.org/en/latest/)
- [Python Reference](https://docs.python.org/3/) for the most recent
  version of Python. (n.b. we are using an old verion, 3.9, on the
  VMs).
- [NumPy for Absolute
  Beginners](https://numpy.org/doc/stable/user/absolute_beginners.html)
- [MatPlotLib](https://matplotlib.org/)
- Literate Programming is a specific instance of the idea that code
  and documentation should be more mixed together. Here is a [Knuth
  paper](http://www.literateprogramming.com/knuthweb.pdf) and an
  [amazing website](http://www.literateprogramming.com/articles.html)
  (not Knuth's) with more information that you ever thought existed on
  program documentation.
- [HDF5](https://docs.hdfgroup.org/hdf5/v1_14/_intro_h_d_f5.html) is a
  file format that supports efficient storage and transfer of numeric
  data.
- [Markdown Cheat
  Sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
- The always useful Software Carpentry [Python
  course](https://swcarpentry.github.io/python-novice-inflammation/)
- All of the [released LIGO data](https://gwosc.org/data/)
