import numpy as np


def oddify_kernel(kernel: np.array) -> np.array:
    if kernel.shape[0] % 2 != 0:
        return kernel
    rows, cols = kernel.shape
    kernel_padded = np.zeros((rows + 1, cols + 1))
    kernel_padded[0: rows, 0: cols] = kernel[0: rows, 0: cols]
    return kernel_padded


def apply_filter_2d(image: np.array, kernel_in: np.array) -> np.array:
    kernel = oddify_kernel(kernel_in)
    rows, cols = image.shape
    kernel_radius = kernel.shape[0]
    kernel_pad = int((kernel_radius - 1) / 2)
    image_padded = np.zeros((rows + kernel_pad * 2, cols + kernel_pad * 2))
    # create a padding around the original image, copy the original image
    image_padded[kernel_pad: rows + kernel_pad, kernel_pad: cols + kernel_pad] = image
    image_final = np.zeros(image.shape)
    for i in range(rows):
        for j in range(cols):
            res = np.einsum('ij,ij->', kernel, image_padded[i: i + kernel_radius, j: j + kernel_radius])
            if res > 255:
                res = 255
            if res < 0:
                res = 0
            image_final[i][j] = int(res)
    return image_final.astype(int)


def apply_filter_3d(image: np.array, kernel_in: np.array) -> np.array:
    kernel = oddify_kernel(kernel_in)
    rows, cols, rgb = image.shape
    kernel_radius = kernel.shape[0]
    kernel_pad = int((kernel_radius-1)/2)
    image_padded = np.zeros((rows + kernel_pad * 2, cols + kernel_pad * 2, rgb))
    # create a padding around the original image, copy the original image
    image_padded[kernel_pad: rows + kernel_pad, kernel_pad: cols + kernel_pad] = image
    image_final = np.zeros(image.shape)
    for i in range(rows):
        for j in range(cols):
            res_r = np.einsum('ij,ij->', kernel, image_padded[i: i + kernel_radius, j: j + kernel_radius, 0])
            res_g = np.einsum('ij,ij->', kernel, image_padded[i: i + kernel_radius, j: j + kernel_radius, 1])
            res_b = np.einsum('ij,ij->', kernel, image_padded[i: i + kernel_radius, j: j + kernel_radius, 2])
            if res_r > 255:
                res_r = 255
            if res_r < 0:
                res_r = 0
            if res_g > 255:
                res_g = 255
            if res_g < 0:
                res_g = 0
            if res_b > 255:
                res_b = 255
            if res_b < 0:
                res_b = 0
            image_final[i][j][0] = int(res_r)
            image_final[i][j][1] = int(res_g)
            image_final[i][j][2] = int(res_b)
    return image_final.astype(int)


def apply_filter(image: np.array, kernel: np.array) -> np.array:
    # A given image has to have either 2 (grayscale) or 3 (RGB) dimensions
    assert image.ndim in [2, 3]
    # A given filter has to be 2 dimensional and square
    assert kernel.ndim == 2
    assert kernel.shape[0] == kernel.shape[1]
    if image.ndim == 2:
        return apply_filter_2d(image, kernel)
    elif image.ndim == 3:
        return apply_filter_3d(image, kernel)
