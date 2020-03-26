from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import torch
from torch.autograd import Variable
import torchvision.transforms as transforms
import numpy as np
from io import BytesIO
from PIL import Image
import time

from nuaa.model import Net


def main():
    try:
        user_name = browser.find_element(By.CSS_SELECTOR, '#ctl00_txtusername')
        password = browser.find_element(By.CSS_SELECTOR, '#ctl00_txtpassword')
        captcha = browser.find_element(By.CSS_SELECTOR, '#ctl00_txtyzm')
        submit_button = browser.find_element(By.CSS_SELECTOR, '#ctl00_ImageButton1')
        user_name.clear()
        password.clear()
        captcha.clear()

        # Get the captcha
        element = browser.find_element(By.CSS_SELECTOR, '#myCode').screenshot_as_png
        captcha_image = Image.open(BytesIO(element)).convert('RGB')
        captcha_num = translate(captcha_image)

        user_name.send_keys('sx1903185')
        password.send_keys('Zxy123456')
        captcha.send_keys(captcha_num)
        time.sleep(2)
        submit_button.click()
        try:
            alert = browser.switch_to.alert
            alert.accept()
            print('fail')
            main()
        except NoAlertPresentException:
            print('succeed')
    finally:
        pass
        # browser.close()


def translate(captcha_image):
    image = captcha_image.resize((160, 60))
    image = transforms(image).unsqueeze(0)
    predict_vector = net(image)[0]
    v1 = image_gen.all_char_set[np.argmax(predict_vector[:s].data.numpy())]
    v2 = image_gen.all_char_set[np.argmax(predict_vector[s: 2 * s].data.numpy())]
    v3 = image_gen.all_char_set[np.argmax(predict_vector[2 * s: 3 * s].data.numpy())]
    v4 = image_gen.all_char_set[np.argmax(predict_vector[3 * s: 4 * s].data.numpy())]
    captcha_num = int(''.join((v1, v2, v3, v4)))
    return captcha_num


if __name__ == '__main__':
    net = Net()
    net.load_state_dict(torch.load('parameters/epoch2.pkl'))
    transforms = transforms.Compose([transforms.Grayscale(), transforms.ToTensor()])
    s = len(image_gen.all_char_set)

    base_url = 'http://gsmis.nuaa.edu.cn/pyxx/login.aspx'
    browser = webdriver.Chrome(executable_path=r'D:\chromewebdriver\chromedriver_win32\chromedriver.exe')
    browser.implicitly_wait(10)
    browser.get(base_url)

    main()