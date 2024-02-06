# CICF Week 3

The goals for week 3 lab are:

1. Install and use the Jupyter notebook application on your VM.
1. Be able to create, edit, and run notebooks.


## Tutorial

When running jobs on many CPUs, we need to take into account how the CPUs communicate with each other.
One way is to share memory, which works up to a point, but doesn't scale past that.
Another way is to have networking and to use something called MPI (for Message Passing Interface) to communicate between processes on different machines.
The computer architecture that works best will depends on the problem you are trying to solve.
Some problems can be framed as many independent operations that only need to synchronize infrequently (e.g. [Science United](https://scienceunited.org/) or SETI @ Home).
These kinds of problems are the easiest to scale up up to massive sizes, since we just need a lot of CPUs, but don't need much in terms of interconnections.
The problems that resist such a framing need many CPUs that are interconnected, and network speed will be a major factor.
These are the problems that supercomputers are designed for.
A lot of these are simulations, where each point in a grid depends on what is happening at other neighboring points.


### Jupyter

OK! Lets look at Python and Jupyter notebooks, an increasingly standard way of using Python.

First, update your cicf files:

    cd cicf
    git pull

We need to install Jupyter on our VMs.
If you didn't do this last week:

    sudo apt install jupyter

Go into week 3 and start juypter:

    cd week3
    jupyter notebook

Select the introduction notebook, `Introduction.ipynb`.
Read through the notebook and run the commands.
When finished look at the tutorial for Python notebook, `QuickTourOfPython.ipynb`, and then the third notebook, `PythonPackages.ipynb`.


## Resources

- The always useful Software Carpentry [Python course](https://swcarpentry.github.io/python-novice-inflammation/)
- [Jupyter Manual](https://docs.jupyter.org/en/latest/)
- [Python Reference](https://docs.python.org/3/) for the most recent version of Python. (n.b. we are using an old verion, 3.9, on the VMs).
- [NumPy for Absolute Beginners](https://numpy.org/doc/stable/user/absolute_beginners.html)
- [MatPlotLib](https://matplotlib.org/)
- Literate Programming is a specific instance of the idea that code and documentation should be more mixed together. Here is a [Knuth paper](http://www.literateprogramming.com/knuthweb.pdf) and an [amazing website](http://www.literateprogramming.com/articles.html) (not Knuth's) with more information that you ever thought existed on program documentation.
- [Markdown Cheat Sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
- A fun [LIGO data tutorial](https://gwosc.org/tutorial02/) and all of the [released LIGO data](https://gwosc.org/data/)
- If you do the LIGO tutorial, the data is a file format called [HDF5](https://docs.hdfgroup.org/hdf5/v1_14/_intro_h_d_f5.html). This format supports efficient storage and transfer of numeric data.

