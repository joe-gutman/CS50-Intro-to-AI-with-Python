# Traffic



## Background
As research continues in the development of self-driving cars, one of the key challenges is computer vision, allowing these cars to develop an understanding of their environment from digital images. In particular, this involves the ability to recognize and distinguish road signs – stop signs, speed limit signs, yield signs, and more.

In this project, you’ll use TensorFlow to build a neural network to classify road signs based on an image of those signs. To do so, you’ll need a labeled dataset: a collection of images that have already been categorized by the road sign represented in them.

Several such data sets exist, but for this project, we’ll use the German Traffic Sign Recognition Benchmark (GTSRB) dataset, which contains thousands of images of 43 different kinds of road signs.

## Getting Started
- Download the distribution code from [here](https://cdn.cs50.net/ai/2020/x/projects/5/traffic.zip) and unzip it.
- Download the data set for this project and unzip it. Move the resulting gtsrb directory inside of your traffic directory.
- Inside of the traffic directory, run `pip3 install -r requirements.txt` to install this project’s dependencies: opencv-python for image processing, scikit-learn for ML-related functions, and tensorflow for neural networks.

## Understanding
First, take a look at the data set by opening the gtsrb directory. You’ll notice 43 subdirectories in this dataset, numbered 0 through 42. Each numbered subdirectory represents a different category (a different type of road sign). Within each traffic sign’s directory is a collection of images of that type of traffic sign.

Next, take a look at `traffic.py`. In the `main` function, we accept as command-line arguments a directory containing the data and (optionally) a filename to which to save the trained model. The data and corresponding labels are then loaded from the data directory (via the `load_data` function) and split into training and testing sets. After that, the `get_model` function is called to obtain a compiled neural network that is then fitted on the training data. The model is then evaluated on the testing data. Finally, if a model filename was provided, the trained model is saved to disk.

The `load_data` and `get_model` functions are left to you to implement.

## Specification
- Complete the implementation of `load_data` and `get_model` in `traffic.py`.
    - The `load_data` function should accept as an argument `data_dir`, representing the path to a directory where the data is stored, and return image arrays and labels for each image in the data set.
        - You may assume that `data_dir` will contain one directory named after each category, numbered 0 through NUM_CATEGORIES - 1. Inside each category directory will be some number of image files.
        - Use the OpenCV-Python module (cv2) to read each image as a numpy.ndarray (a numpy multidimensional array). To pass these images into a neural network, the images will need to be the same size, so be sure to resize each image to have width `IMG_WIDTH` and height `IMG_HEIGHT`.
        - The function should return a tuple `(images, labels)`. `images` should be a list of all of the images in the data set, where each image is represented as a numpy.ndarray of the appropriate size. `labels` should be a list of integers, representing the category number for each of the corresponding images in the `images` list.
        - Your function should be platform-independent: that is to say, it should work regardless of operating system. Note that on macOS, the `/` character is used to separate path components, while the `\` character is used on Windows. Use `os.sep` and `os.path.join` as needed instead of using your platform’s specific separator character.
    - The `get_model` function should return a compiled neural network model.
        - You may assume that the input to the neural network will be of the shape `(IMG_WIDTH, IMG_HEIGHT, 3)` (that is, an array representing an image of width `IMG_WIDTH`, height `IMG_HEIGHT`, and 3 values for each pixel for red, green, and blue).
        - The output layer of the neural network should have `NUM_CATEGORIES` units, one for each of the traffic sign categories.
        - The number of layers and the types of layers you include in between are up to you. You may wish to experiment with:
            - different numbers of convolutional and pooling layers
            - different numbers and sizes of filters for convolutional layers
            - different pool sizes for pooling layers
            - different numbers and sizes of hidden layers
            - dropout

## Hints
- Check out the [official Tensorflow Keras overview](https://www.tensorflow.org/guide/keras/sequential_model) for some guidelines for the syntax of building neural network layers. You may find the lecture source code useful as well.
- The [OpenCV-Python documentation](https://docs.opencv.org/3.4/) may prove helpful for reading images as arrays and then resizing them.
- Once you’ve resized an image `img`, you can verify its dimensions by printing the value of `img.shape`. If you’ve resized the image correctly, its shape should be `(30, 30, 3)` (assuming `IMG_WIDTH` and `IMG_HEIGHT` are both 30).
- If you’d like to practice with a smaller data set, you can download a modified dataset that contains only 3 different types of road signs instead of 43.
