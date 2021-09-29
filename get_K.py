import numpy as np
from PIL import Image

# load the image and convert it to a numpy array
image = np.array(Image.open('PyJulR2.bmp'))

# threshold the image: convert the array to binary and then back to int
image = image.astype(bool).astype(int)

# transpose (image must be encoded column-wise), mirror (to match original coordinates frame) and flatten
image = np.fliplr(image.T).flatten()

# represent array as one integer in base 10 and multiply it by 17
K = int(''.join(map(str, image)), 2) * 17

# for readability let's split the found number by 3 characters
from textwrap import wrap
print(f'Found K: {" ".join(wrap(str(K), 3))}')