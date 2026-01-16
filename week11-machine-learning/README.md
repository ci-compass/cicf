# CICF Week 11

This week, we will look at some data wrangling on a tabular dataset.
We will then fit a decision tree and a random forest models to the data.

## Tutorial

This class focuses more on the tools and concepts you might encounter related to cyberinfrastructure.
This means we are not going to cover the mathematics behind the machine learning algorithms in much depth.
However, I encourage you to look at these materials if you find the techniques interesting.
This tutorial and the next are based on the Practical Deep Learning for Coders lessons by Jeremy Howard. References are included in the [Resources](#Resources) section at the end of this file.

### Random Forests

This section is modeled after the excellent tutorial by Jeremy Howard, titled
["How Random Forests Really Work"](https://www.kaggle.com/code/jhoward/how-random-forests-really-work/).
I recommend looking at this for more detail on how decision trees and random forests work.

Open your VM, and `git pull` in the `cicf` folder. Then run:

    $ sudo apt install graphviz
    $ pip install --upgrade jupyter-core nbconvert seaborn fastai

We are going to work with the [Titanic dataset](https://github.com/datasciencedojo/datasets/blob/master/titanic.csv).
This dataset is a passenger manifest from the Titanic, and is a common one for machine learning examples.
It contains both continuous and categorical values, and isn't too big.

The rest of this section is in the notebook [random-forest.ipynb](random-forest.ipynb).

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
