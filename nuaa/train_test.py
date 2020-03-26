import matplotlib.pyplot as plt
import torch
import torch.nn as nn
from torch.autograd import Variable
import numpy as np
import time

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


def train():
    running_loss = 0
    total = 0
    correct = 0
    for i, (images, true_vectors) in enumerate(train_dataloader):
        optimizer.zero_grad()
        predict_vectors = net(images)
        loss = m_loss(predict_vectors, true_vectors)
        loss.backward()
        optimizer.step()
        running_loss += loss

        predict_labels = tensor_vector_to_label(predict_vectors)
        labels = [ohe.decode(true_vector.numpy()) for true_vector in true_vectors]
        total += len(labels)
        for predict_label, true_label in zip(predict_labels, labels):
            # print(predict_label, true_label)
            if predict_label == true_label:
                correct += 1

        if (i + 1) % 100 == 0:
            print('epoch %d step %d loss %.5f' % (epoch+1, i+1, running_loss / 100))
            loss_list.append(running_loss / 100)
            running_loss = 0
    torch.save(net.state_dict(), 'parameters/epoch%d.pkl' % (epoch+1))
    print('Epoch %d train accuracy: %d / %d = %f' % (epoch + 1, correct, total, correct / total))


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
                if predict_label == true_label:
                    correct += 1
    print('Epoch %d test accuracy: %d / %d = %f' % (epoch + 1, correct, total, correct / total))
    acc_list.append(correct / total)


if __name__ == '__main__':
    s = len(image_gen.all_char_set)
    batch_size = 64
    num_epochs = 30

    net = Net()
    optimizer = torch.optim.Adam(net.parameters())
    m_loss = nn.MultiLabelSoftMarginLoss()
    train_dataloader = dataset.get_train_data_loader(batch_size=batch_size)
    test_dataloader = dataset.get_test_data_loader(batch_size=batch_size)
    loss_list = []
    acc_list = []
    for epoch in range(num_epochs):
        train()
        test()
    print(acc_list)
    plt.plot(loss_list)
    plt.savefig('training-loss.png')
