# CICF Week 11

This week, we will look at some data wrangling on a tabular dataset.
We will then fit a decision tree and a random forest models to the data.

## Tutorial

This class focuses more on the tools and concepts you might encounter related to cyberinfrastructure.
This means we are not going to cover the mathematics behind the machine learning algorithms in much depth.
However, I encourage you to look at these materials if you find the techniques interesting.
This tutorial and the next are based on the Practical Deep Learning for Coders lessons by Jeremy Howard.
References are included in the [Resources](#Resources) section at the end of this file.

### tar.gz

A file format you will probably see are `.tar.gz` files.
This file is actually two pieces: a "tar" file, which groups many files together, just like a primitive ZIP file;
and the whole thing is compressed using the GZIP compression algorithm.
You can work with them with the `tar` command:

To untar everything into the current directory:

    tar xvfz my-file.tar.gz

To list the files in the tar file

    tar tvfz my-file.tar.gz

(Why are they a primitive form of a ZIP file? Because a zip file has a _central directory_ at the end which
is an index to all the files stored inside it.
Tar files do not have that; they are just a long sequence and there is no way to extract an individual file
without starting at the beginning.)

### Random Forests and NEON Data

Lets install some python packages

    $ sudo apt update
    $ sudo apt install graphviz
    $ source .venv/bin/activate
    $ pip install --upgrade jupyter-core nbconvert seaborn scikit-learn boto3 python-dotenv

We are going to work with mosquito data collected by the National Ecological Observatory Network (NEON).
The data is hosted on the CICF cloud storage in Digital Ocean.

In your group, you will:
1. Download the dataset using `boto3`.
2. Clean and preprocess the data.
3. Train a Random Forest model to predict mosquito counts.

The activity is in the notebook [mosquito-random-forest.ipynb](mosquito-random-forest.ipynb).

## Resources

Sources for this tutorial:

- [Random Forests - Practical Deep Learning for Coders](https://course.fast.ai/Lessons/lesson6.html)
- ["How Random Forests Really Work"](https://www.kaggle.com/code/jhoward/how-random-forests-really-work/).
- [Neural Net Foundations](https://course.fast.ai/Lessons/lesson3.html)

Other interesting links:

- [Google Colab](https://colab.research.google.com/) provides a Jupyter notebook-like interface on top of a cloud computing platform. Definitely worth looking at.
- [Titanic - Machine Learning from Disaster](https://www.kaggle.com/competitions/titanic/data) is the Kaggle competition I mentioned.- [Astronomers Dig Up the Stars That Birthed the Milky Way](https://www.quantamagazine.org/with-ai-astronomers-dig-up-the-stars-that-birthed-the-milky-way-20230328/)
- [Cornell Machine Learning Course](https://www.cs.cornell.edu/courses/cs4780/2015fa/page4/)
- [Google Machine Learning Course](https://developers.google.com/machine-learning/crash-course/ml-intro)
- [Library of Statistical Techniques](https://lost-stats.github.io/)
- [Bias-Variance Tradeoff](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff)
- [UC Irvine Machine Learning Repository](https://archive-beta.ics.uci.edu/) has a bunch of datasets.
