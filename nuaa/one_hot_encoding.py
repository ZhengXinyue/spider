import numpy as np
from . import image_gen


def encode(text):
    vector = np.zeros(image_gen.max_captcha * len(image_gen.all_char_set))
    for i, s in enumerate(text):
        idx = i * len(image_gen.all_char_set) + int(s)
        vector[idx] = 1
    return vector


def decode(vector):
    nums = vector.nonzero()[0]
    for i in range(len(nums)):
        nums[i] -= i * 10
    return ''.join(str(i) for i in nums)


if __name__ == '__main__':
    a = encode('0000')
    print(a)
    m = decode(a)
    print(m)
