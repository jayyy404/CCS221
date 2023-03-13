#Group 4
#John Paul Sapasap
#Jed Andrew Del Rosario
#Marc Joshua Escueta

import cv2
import numpy as np
import matplotlib.pyplot as plt

def read_image(path):
    img = cv2.imread(path)
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def translate_image(img, bx, by):
    rows, cols = img.shape[:2]
    m = np.float32([[1, 0, bx], [0, 1, by]])
    return cv2.warpAffine(img, m, (cols, rows))

def new_translated(img, bx_old, by_old, tx, ty):
    bx_new = bx_old + tx *10
    by_new = by_old + ty*10
    return translate_image(img, bx_new, by_new)

def main():
    # Read image
    img = read_image("test.jpg")

    # IMAGES WITH ORIGINAL VALUES
    translated_imgs = []
    for bx, by in zip(range(2, 7), range(5, 10)):
        translated_imgs.append(translate_image(img, bx, by))

    # IMAGES WITH NEW VALUES
    modified_imgs = []
    for bx_old, by_old, tx, ty in [(2, 5, 6, 2), (3, 6, 7, 3), (4, 7, 8, 4), (5, 8, 9, 5), (6, 9, 10, 3)]:
        modified_imgs.append(new_translated(img, bx_old, by_old, tx, ty))

    # Display images
    fig, axs = plt.subplots(2, 5, figsize=(16, 8))
    for i in range(5):
        axs[0][i].imshow(translated_imgs[i])
        axs[0][i].set_title(f"Original {i+1}")
        axs[1][i].imshow(modified_imgs[i])
        axs[1][i].set_title(f"# {i+1}")
    plt.show()

main()