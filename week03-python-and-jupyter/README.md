# CICF Week 2

The goals for week 2 lab are:

1. Install and use the Jupyter notebook application on your VM.
2. Be able to create, edit, and run notebooks.
3. Use the NumPy and MatPlotLib packages.
4. Download data from LIGO and know what an HDF5 file is.

Start your VM, launch a terminal, and be prepared to run a few
commands in that terminal.

## Update your copy of CICF repository

You should have done a `git clone` of the CICF repository in the home
directory of your VM in the first week itself.  In case you have not
done that yet, go back to the [previous week's instructions][week1],
and follow the instructions under the section titled "Git" there.

[week1]: ../week01-commandline/README.md#Git

Since we will be updating the repository throughout the course, you
will have to make sure you have the latest changes in your local copy.
Change to `~/cicf` directory and then do a `git pull`:

```console
cd ~/cicf
git pull
```

## Install some software

We need to install some Debian packages on our VM using the [apt]
package manager.  But first, we need to run an `apt update` to update
package information from Debian's software repositories.

```console
sudo apt update
```

Enter the password when prompted.

Once that is done, run the next command:

```console
sudo apt install python3-pip python3-venv wget
```

Type `Y` to confirm installation.

We will also need some additional Python packages. These we can
install using [pip], inside what is called a "virtual environment".
Create a virtual environment and activate it with these commands:

```console
python3 -m venv ~/venv
source ~/venv/bin/activate
```

If that worked, you should see a prompt like:

```console
(venv) cicf@debian: $
```

Now install the Python packages:

```console
pip install jupyter numpy scipy matplotlib h5py
```

[apt]: https://wiki.debian.org/AptCLI
[pip]: https://pip.pypa.io/en/stable/

The table below lists the software packages we just installed.

| package            | description                                                                  |
|:-------------------|:-----------------------------------------------------------------------------|
| [python3-pip][pip] | Python package installer                                                     |
| [python3-venv]     | Python module for working with virtual environments on Debian/Ubuntu systems |
| [wget]             | Command-line program used to download files                                  |
| [jupyter]          | An interactive computing environment                                         |
| [numpy]            | Python library for multidimensional arrays, matrices, etc.                   |
| [scipy]            | Python library for scientific computing                                      |
| [matplotlib]       | Python 2D plotting library                                                   |
| [h5py]             | Python library to work with [HDF5] data                                      |

[python3-venv]: https://packages.debian.org/bookworm/python3-venv
[wget]: https://www.gnu.org/software/wget/
[jupyter]: https://jupyter.org/
[numpy]: https://numpy.org/
[scipy]: https://scipy.org/
[matplotlib]: https://matplotlib.org/
[h5py]: https://www.h5py.org/

### A note about virtual environments

Virtual environments allow you to install Python packages in a
location that is isolated from the rest of the system.  This way, when
you install Debian packages written in Python using `apt`, they will
not conflict with the packages you installed using `pip` for your
projects.

Typically, for each of your Python projects, you will create its own
lightweight, isolated virtual environment, usually inside the project
directory.  And then you will install the packages each project need
in its own virtual environment.

(Although in this tutorial, you will note that you just set up a
virtual environment in your home directory. This should work just fine
for us, for now.)

You can figure out details eventually.  For now just bear in mind that
virtual environments are a solution to a problem that you are very
likely to encounter in the future. Here are both a
[friendly explanation][venv-realpython], and
[official documentation][venv-pythonorg].

[venv-pythonorg]: https://docs.python.org/3/library/venv.html
[venv-realpython]: https://realpython.com/python-virtual-environments-a-primer/


## Run Jupyter

Go to `week02-python-and-jupyter` directory in your CICF repository
clone using `cd` command, and then start Jupyter.
(This is a good time to try using the tab completion).

```console
cd ~/cicf/week02-python-and-jupyter
jupyter notebook
```

A browser window will open, listing the contents of
`week02-python-and-jupyter` directory, where you will find some files
with `.ipynb` extension.  They are the Jupyter notebooks that we will
use this week.

<!-- TODO: update this screenshot -->

![Jupyter](./img/jupyter.png)

Working through these notebooks is your task this week:

- [1-introduction.ipynb](./1-introduction.ipynb) is an introduction to
  Jupyter.
- [2-quick-python-tour.ipynb](./2-quick-python-tour.ipynb) is a quick
  introduction of Python programming language.
- [3-python-packages.ipynb](./3-python-packages.ipynb) is an overview
  of Python packages.
- [4-plot-ligo-data.ipynb](./4-plot-ligo-data.ipynb) is a notebook
  that will walk you through working with some science data in
  Jupyter.

You can open each these notebooks by double clicking them, or by
clicking on the "open" button that will appear when you select a
notebook.

### JupyterLab

JupyterLab is a newer, fancier, and perhaps nicer way to interact with
Jupyter notebooks.  You can launch a JupyterLab instance instead of
old notebook interface, with the command:

```console
jupyter lab
```

<!-- TODO: add JupyterLab screenshot -->

Perhaps you might prefer JupyterLab.  You are likely to come across
JupyterLab instances hosted by various organizations and projects.
Some examples:

- [Microsoft Planetary Computer](https://planetarycomputer.microsoft.com/)
- [FABRIC project's JupyterLab instance](https://jupyter.fabric-testbed.net/)
- [Chameleon project's JupyterLab instance](https://jupyter.chameleoncloud.org/)

Google [Colab] also supports Jupyter notebooks.

[Colab]: https://colab.research.google.com/

In fact, you can open this week's notebooks straight in Colab.  Try
these links:

- https://colab.research.google.com/github/ci-compass/cicf/blob/main/week02-python-and-jupyter/1-introduction.ipynb
- https://colab.research.google.com/github/ci-compass/cicf/blob/main/week02-python-and-jupyter/2-quick-python-tour.ipynb
- https://colab.research.google.com/github/ci-compass/cicf/blob/main/week02-python-and-jupyter/3-python-packages.ipynb
- https://colab.research.google.com/github/ci-compass/cicf/blob/main/week02-python-and-jupyter/4-plot-ligo-data.ipynb

To run the cells, you will have to sign using a Google account.

However, note that you won't be able to run commands such as `pip` and
`wget` in a Colab terminal as we discuss here: in order to be able to
use a terminal, Colab requires a paid plan.  So you probably won't be
able to run all the cells in the third and fourth notebooks.

But that is just an irrelevant detail for now.  You already have a
virtual machine set up to do what you need to do!

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

## Note to the staff (and to the curious)

The Jupyter notebooks in this directory are generated from the `.qmd`
files in the `qmd/` directory, using [Quarto]. See `qmd/Makefile` for
the steps involved. Quarto project calls `.qmd` files "computational
markdown".  They are markdown but with some syntax enhancements.

The first three were the original notebooks from CICF year 3 written
by Erik Scott, and I (Sajith S) converted them to markdown to Quarto.

I am doing things this way because I would rather be using a text
editor than anything else.  Future maintainers of these lessons should
be free to choose whichever format they prefer.

[Quarto]: https://quarto.org/
