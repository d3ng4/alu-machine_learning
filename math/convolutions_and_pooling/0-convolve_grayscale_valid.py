#!/usr/bin/env python3


import numpy as np


def convolve_grayscale_valid(images, kernel):
    """
    Convolves a set of grayscale images with a given kernel using valid padding.

    Args:
        images (numpy.ndarray): Input grayscale images. Shape: (m, h, w), where m is the number of
            images, h is the height, and w is the width.
        kernel (numpy.ndarray): Convolution kernel. Shape: (kh, kw), where kh is the kernel height
            and kw is the kernel width.

    Returns:
        numpy.ndarray: Convolved images. Shape: (m, h - kh + 1, w - kw + 1).

    Raises:
        ValueError: If the dimensions of the images and kernel are incompatible.
    """
    m, h, w = images.shape
    kh, kw = kernel.shape

    convolved_images = np.zeros((m, h - kh + 1, w - kw + 1))

    for i in range(h - kh + 1):
        for j in range(w - kw + 1):
            convolved_images[:, i, j] = np.sum(
                images[:, i:i+kh, j:j+kw] * kernel, axis=(1, 2))

    return convolved_images
