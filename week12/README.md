# CICF Week 12

This week we will cover what a neural network is.
We will build a simple model for the same tabular data as in week 11,
and then we will look at applications of neural networks to images.

## Tutorial

In the Excel sheet we took our dataset and produced 11 numeric columns.
We then made two sets of weights and multiplied the columns by them to get two numbers.
We then took these two numbers, replaced any negatives with 0 and added them together.
This sum was then used to make our survival prediction.
We then used the Excel solve function to adjust the weights to minimize our loss function—which is a function we used to measure how close each prediction is to being correct.
Amazingly, this worked well enough to get a 80% accuracy rate.

Lets think about how we would go about optimizing the weights ourselves.
Suppose we are looking at a specific row in our dataset.
We can feed the data into our function and look at the prediction, and calculate the loss function for it.
We then ask, "if I were to adjust the first weight, how much would the loss function change?"
This is the same question as asking what the deritivie of our prediction + loss function is with respect to the first weight.
And we can calculate this since each step of the calculation process is differentiable (or close enough in the case of the `max` function).

We have the computer calculate the deriative with respect to each weight, and then we adjust all the weights up or down so as to decrease the loss function.

We are now going to look at the first notebook [basic_neural_network.ipynb](basic_neural_network.ipynb) to see how a common Python framework called PyTorch can be used to create the same model that we have in the spreadsheet.
This section was based on the following (more detailed and much better) notebook:
https://github.com/fastai/course22/blob/master/05-linear-model-and-neural-net-from-scratch.ipynb

Once we have looked at making a linear network, we will look at image classification.
This is in the second notebook [mnist.ipynb](mnist.ipynb).
Again, this is based in part on two other excellent notebooks
[mnist_basics](https://github.com/fastai/fastbook/blob/master/04_mnist_basics.ipynb) and
[convolutions](https://github.com/fastai/fastbook/blob/master/13_convolutions.ipynb)

## Resources

- 3Blue1Brown [video illustrating backpropagation](https://www.youtube.com/watch?v=tIeHLnjs5U8) is an excellent introduction to the math behind training neural networks.
- This is a great mini-implementation of a gradiant calculating framework for training a NN. [Karpathy's "micrograd"](https://github.com/karpathy/micrograd/blob/master/demo.ipynb). He also has a great [lesson notebook introducing it](https://github.com/karpathy/nn-zero-to-hero/blob/master/lectures/micrograd/micrograd_lecture_first_half_roughly.ipynb)
- [Fast AI Practical Deep Learning](https://course.fast.ai/)
- [Data Ethics](https://ethics.fast.ai/)
- There is a great need to have metadata tracking who made all these neural network models, the kinds of data used to train them, and the licencing for how others can reuse the models. [Model Card Annotated](https://huggingface.co/docs/hub/en/model-card-annotated) describes one approach to standardizing this.
- [MNIST Visualization](https://colah.github.io/posts/2014-10-Visualizing-MNIST/)
- [How does a neural net really work?](https://www.kaggle.com/code/jhoward/how-does-a-neural-net-really-work)
- [Looking inside neural nets](https://ml4a.github.io/ml4a/looking_inside_neural_nets/) is a fun article discussing and showing how image decoding works.
- [A Visual Guide to Vision Transformers](https://blog.mdturp.ch/posts/2024-04-05-visual_guide_to_vision_transformer.html)
