# CICF Week 3

The goals for week 2 lab are:

1. Install and use the Jupyter notebook application on your VM.
1. Be able to create, edit, and run notebooks.
1. 



## Tutorial

We need to install Jupyter on our VMs:

    sudo apt install jupyter

Type `Y` to confirm installation.
When it is finished, start Jupyter with the command

    jupyter notebook

You will see a browser window open displaying your filesystem.
Navigate to `cicf/week3/introduction.ipynb` and open it.

A Jupyter notebook consists of a bunch of _cells_ which contain either text (in [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) format), or python code and its output.

The python code is _runnable_, which means you can select a python cell and then choose the menu option "Cell > Run Cells".
Try running both of the python cells in the notebook.

Commands to try:

    56

This produces an output. Notice the python input and output cells are numbered in the order that they are run.

    56+7

The python cells will evaluate the expression and return its value

    print("hello")

Note that `print()` is an expression that outputs something the the screen and then return the value `None`.

    import math

    2*math.PI*5

The last command has an error. We can fix it and rerun the cell. It should be `2*math.pi*5`.


    sudo apt install python3-pip
    pip3 install numpy




## Resources

- Jupyter Manual
- Literate Programming
- Python Reference
- NumPy
- SciPy
- MatPlotLib

