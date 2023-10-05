#!/usr/bin/env python3


import numpy as np


def convolve_grayscale_same(images, kernel):
    """
    Convolves a set of grayscale images with a given kernel using same padding.
    """
    m, h, w = images.shape
    kh, kw = kernel.shape

    # Calculate the padding sizes
    pad_h = kh // 2
    pad_w = kw // 2

    # Pad the images with zeros
    padded_images = np.pad(
        images, ((0, 0), (pad_h, pad_h), (pad_w, pad_w)), mode='constant'
    )

    convolved_images = np.zeros_like(images)

    for i in range(h):
        for j in range(w):
            convolved_images[:, i, j] = np.sum(
                padded_images[:, i:i+kh, j:j+kw] * kernel, axis=(1, 2)
            )

    return convolved_images
