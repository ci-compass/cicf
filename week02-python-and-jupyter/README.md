# CICF Week 3

The goals for week 3 lab are:

1. Install and use the Jupyter notebook application on your VM.
2. Be able to create, edit, and run notebooks.
3. Use the NumPy and MatPlotLib packages.
4. Download data from LIGO and know what an HDF5 file is.


## Getting set up

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

If you are confused about the software we just installed, the below
table might help:

| package            | description                                                |
|:-------------------|:-----------------------------------------------------------|
| [python3-pip][pip] | Python package installer                                   |
| [wget]             | Command-line program used to download files                |
| [jupyter]          | An interactive computing environment                       |
| [numpy]            | Python library for multidimensional arrays, matrices, etc. |
| [scipy]            | Python library for scientific computing                    |
| [matplotlib]       | Python 2D plotting library                                 |
| [h5py]             | Python library to work with [HDF5] data                    |

[wget]: https://www.gnu.org/software/wget/
[jupyter]: https://jupyter.org/
[numpy]: https://numpy.org/
[scipy]: https://scipy.org/
[matplotlib]: https://matplotlib.org/
[h5py]: https://www.h5py.org/

### A note about virtual environments

Note that when you do `pip install jupyter numpy scipy matplotlib
h5py` (as we have done above), they will get installed in a folder in
your home directory.

This will work just fine for now, but over time this will become
messy.  You will install packages which will need to install other
packages that have conflicting requirements. You will install
different versions of Python, which probably will not work with the
packages you have installed already.  You will encounter conflicts,
and you will have to clean up the mess.

To avoid the mess, you will use what is called a _virtual
environment_, usually inside your project directory.  For each of your
Python projects, you will create its own lightweight, isolated virtual
environment. You will install the packages each project need in their
own virtual environment.

We can figure out the details later. For now just bear in mind that
virtual environments are a solution to a problem that you are likely
to encounter in the future. You can find a friendly explanation
[here](venv-realpython), and official documentation
[here](venv-pythonorg).

[venv-pythonorg]: https://docs.python.org/3/library/venv.html
[venv-realpython]: https://realpython.com/python-virtual-environments-a-primer/


### Checking out CICF repository

You should have cloned the CICF git repository in the home directory
of your VM in the first week itself.  In case you have not done that
yet, do this:

```console
git clone https://github.com/ci-compass/cicf ~/cicf
```

We will keep updating the repository throughout the course. Make sure
you have the latest changes by changing to `~/cicf` directory and then
doing a `git pull`:

```console
cd ~/cicf
git pull --autostash
```

## Run Jupyter

Go to `week03` directory in your CICF repository clone using `cd`
command, and then start Jupyter with the command below:

```console
cd ~/cicf/week03
jupyter notebook
```

A browser window will open, listing the contents of `~/cicf/week03`
directory, where you will find four files with `.ipynb` extension.
They are the Jupyter notebooks that we will use this week.  Let us
work through them in sequence.

### The first notebook: introduction to Jupyter

Open [1-introduction.ipynb](./introduction.ipynb) by double clicking
on it.  The notebook will open in a new browser tab.

A Jupyter notebook consists of a bunch of _cells_ which contain either
code or text (in [Markdown] format) and its output.  In CICF examples
we will (mostly?) use Python code in our examples, but it is possible
to use other programming languages also in Jupyter notebooks.

(A fun fact: the name Jupyter is an amalgamation of [Julia], Python,
and [R] -- the three programming languages supported by Jupyter.)

[Markdown]: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
[Julia]: https://julialang.org/
[R]: https://www.r-project.org/

The code in the notebooks is _runnable_, directly from the browser
window.  You can select a python cell and then choose the menu option
"Cell > Run Cells".  Follow the text along, and try out the
instructions to run the code present in the notebook.

### The second notebook: a quick tour of Python

You can also create new code cells in this notebook, and write some
code in those cells, and try running them.

This is a line of code:

```python
42
```

Running a cell with the above code produces an output. Notice the
python input and output cells are numbered in the order that they are
run.

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

### The third notebook: Python packages

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

### The fourth notebook: working with LIGO data

In this part of the tutorial, let us plot some data from the LIGO observatory.  

#### Getting a LIGO dataset

Go to the the `week03` directory of your CICF repository clone, and
then run `wget` with the URL of the data set as its argument (as shown
below).

```console
cd ~/cicf/week03
wget https://gwosc.org/archive/data/S5/814743552/H-H2_LOSC_4_V1-815235072-4096.hdf5
```

That should download a file `H-H2_LOSC_4_V1-815235072-4096.hdf5`,
which is about 123MB in size.  This file is in a format called [HDF5],
commonly used to store scientific data.  We will use the Python h5py
package that we installed earlier to work with this file.

[HDF5]: https://en.wikipedia.org/wiki/Hierarchical_Data_Format

Open [4-plot-ligo-data.ipynb](./4-plot-ligo-data.ipynb) in your
Jupyter environment, and work through the notebook.


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
