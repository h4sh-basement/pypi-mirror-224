import numpy as np
from scipy.misc import ascent
from augmend.transforms.affine import transform_rotation
from augmend.utils import create_test_pattern
from time import time

if __name__ == '__main__':
    img = create_test_pattern()


    out = transform_rotation(img, offset = (40,40))

    import matplotlib.pyplot as plt
    plt.ion()
    plt.figure(1)
    plt.clf()
    plt.imshow(out)
    plt.show()


    
