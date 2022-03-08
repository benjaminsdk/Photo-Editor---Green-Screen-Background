from scipy import misc,ndimage
import matplotlib.pyplot as plt
import numpy as np
import imageio


def image_composition(filename1, filename2):
    characters = imageio.imread(filename1)
    background = imageio.imread(filename2)

    for i in range(characters.shape[0]):
        for j in range(characters.shape[1]):
            if characters[i][j][1]>180 and characters[i][j][1]>characters[i][j][2] and characters[i][j][1]>characters[i][j][0]:
                characters[i][j]=background[i][j]
    plt.imshow(characters)
    plt.show()
    plt.savefig('NewImage.jpg')

image_composition('lion.jpg','snow.jpg')
