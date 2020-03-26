import os
from PIL import Image
from torch.utils.data import DataLoader, Dataset
import torchvision.transforms as transforms

import nuaa.one_hot_encoding as ohe


class Mydataset(Dataset):
    def __init__(self, folder, transform=None):
        super(Mydataset, self).__init__()
        self.train_image_file_paths = [os.path.join(folder, image_file) for image_file in os.listdir(folder)]
        self.transform = transform

    def __len__(self):
        return len(self.train_image_file_paths)

    def __getitem__(self, item):
        image_abs_path = self.train_image_file_paths[item]
        image = Image.open(image_abs_path)
        if self.transform:
            image = self.transform(image)

        image_name = image_abs_path.split(os.path.sep)[-1]
        text = image_name.split('_')[0]
        label = ohe.encode(text)
        return image, label


transforms = transforms.Compose([transforms.Grayscale(), transforms.ToTensor()])


def get_train_data_loader(batch_size):
    dataset = Mydataset(image_gen.train_data_path, transform=transforms)
    return DataLoader(dataset, batch_size=batch_size, shuffle=True)


def get_test_data_loader(batch_size):
    dataset = Mydataset(image_gen.test_data_path, transform=transforms)
    return DataLoader(dataset, batch_size=batch_size, shuffle=True)



