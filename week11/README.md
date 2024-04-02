# CICF Week 11

## Tutorial

This class focuses more on the tools and concepts you might encounter related to cyberinfrastructure.
This means we are not going to cover the mathematics behind the machine learning algorithms in much depth.
But I encourage you to look at these materials if you find the techniques interesting.
This and the next tutorials are based on the Practical Deep Learning for Coders lessons by Jeremy Howard. References are included in the [Resources](#Resources) section at the end of this file.

### Random Forests

This section is modeled after the excellent tutorial by Jeremy Howard titled
["How Random Forests Really Work"](https://www.kaggle.com/code/jhoward/how-random-forests-really-work/).
I recommend looking at this for more detail on how decision trees and random forests work.

Open your VM, and `git pull` in the `cicf` folder.

    sudo apt install graphviz
    pip install --upgrade jupyter-core nbconvert seaborn fastai

We are going to work with the Titanic dataset.
Lets first look at the [dataset](https://github.com/datasciencedojo/datasets/blob/master/titanic.csv)
This dataset is a passenger manifest from the Titanic.

The rest of this section is in the notebook `random-forest.ipynb`.

## Resources

- [Astronomers Dig Up the Stars That Birthed the Milky Way](https://www.quantamagazine.org/with-ai-astronomers-dig-up-the-stars-that-birthed-the-milky-way-20230328/)
- [Cornell Machine Learning Course](https://www.cs.cornell.edu/courses/cs4780/2015fa/page4/)
- [Google Machine Learning Course](https://developers.google.com/machine-learning/crash-course/ml-intro)
- [Visualization](https://colah.github.io/posts/2014-10-Visualizing-MNIST/)

- [Random Forests - Practical Deep Learning for Coders](https://course.fast.ai/Lessons/lesson6.html)

- [Google Colab](https://colab.research.google.com/) provides a Jupyter notebook-like interface on top of a cloud computing platform. Definately worth looking at.

https://github.com/fastai/fastbook/blob/master/04_mnist_basics.ipynb
