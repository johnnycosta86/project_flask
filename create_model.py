import tensorflow as tf
import numpy as np
from imageio import imsave

fashion_mnist = tf.keras.datasets.fashion_mnist

(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

print("X-train {}".format(x_train.shape))
print("Y-train {}".format(y_train.shape))
print("X-test {}".format(x_test.shape))
print("Y-test {}".format(y_test.shape))

print(np.unique(y_test))

# Salva 5 imagens de testes no diretorio uploads
for i in range(5):
    imsave("uploads/{}.png".format(i), x_test[i])