import torch
from torch.autograd import Variable
import numpy as np

from . import dataset
from .model import Net
import nuaa.one_hot_encoding as ohe
import image_gen


def tensor_vector_to_label(vectors):
    labels = []
    for vector in vectors:
        v1 = image_gen.all_char_set[np.argmax(vector[:s].data.numpy())]
        v2 = image_gen.all_char_set[np.argmax(vector[s: 2 * s].data.numpy())]
        v3 = image_gen.all_char_set[np.argmax(vector[2 * s: 3 * s].data.numpy())]
        v4 = image_gen.all_char_set[np.argmax(vector[3 * s: 4 * s].data.numpy())]
        label = ''.join((v1, v2, v3, v4))
        labels.append(label)
    return labels


def test():
    total = 0
    correct = 0
    with torch.no_grad():
        for i, (images, labels) in enumerate(test_dataloader):
            predict_vectors = net(images)
            predict_labels = tensor_vector_to_label(predict_vectors)
            labels = [ohe.decode(label.numpy()) for label in labels]
            total += len(labels)
            for predict_label, true_label in zip(predict_labels, labels):
                print(predict_label, true_label)
                if predict_label == true_label:
                    correct += 1
    print('Epoch %d test accuracy: %d / %d = %f' % (epoch+1, correct, total, correct / total))
    acc_list.append(correct / total)


if __name__ == '__main__':
    net = Net()
    epoch = 7
    net.load_state_dict(torch.load('parameters/epoch%d.pkl' % epoch))
    s = len(image_gen.all_char_set)
    test_dataloader = dataset.get_test_data_loader(batch_size=64)
    acc_list = []
    test()
    print(acc_list)