import os
import random
import time

from captcha.image import ImageCaptcha
from PIL import Image


all_char_set = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
max_captcha = 4
image_width = 160
image_height = 60
train_data_path = 'dataset' + os.path.sep + 'train'
test_data_path = 'dataset' + os.path.sep + 'test'


def random_captcha():
    captcha_text = []
    for i in range(max_captcha):
        captcha_text.append(random.choice(all_char_set))
    return ''.join(captcha_text)


def text_to_image():
    image_func = ImageCaptcha(width=image_width, height=image_height)
    text = random_captcha()
    image = Image.open(image_func.generate(text))
    return text, image


def data_gen(image_num, path):
    if not os.path.exists(path):
        os.makedirs(path)
    for i in range(image_num):
        now = str(int(time.time()))
        text, image = text_to_image()
        filename = ''.join((text, '_', now, '.png'))
        image.save(''.join((path, os.path.sep, filename)))


if __name__ == '__main__':
    data_gen(20000, train_data_path)
    data_gen(2000, test_data_path)
