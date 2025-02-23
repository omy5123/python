import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn import preprocessing,model_selection


# 문제
# mnist 데이터에 대해 소프트맥스 리그레션으로 검사 데이터에 대해 정확도를 구하세요.


data = tf.keras.datasets.mnist.load_data()
(x_train, y_train), (x_test,y_test) = data

print(x_train.shape, x_test.shape)  # (60000, 28, 28) (10000, 28, 28)
print(y_train.shape, y_test.shape)  # (60000,) (10000,)

x_train = x_train.reshape(-1, 784)
x_test = x_test.reshape(-1, 784)

print(np.min(x_train), np.max(x_train))     # 0 255

# 피처별로 스케일링을 하기 때문에 버그의 소지가 있음
# x_train = preprocessing.minmax_scale(x_train)
# x_test = preprocessing.minmax_scale(x_test)

# 올바른 스케일링
x_train = x_train / 255
x_test = x_test / 255

# ----------------------------- #

# 784 -> 256 -> 256 -> 10
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(256, activation='relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(256, activation='relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(10, activation='softmax'))

model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.001),
              loss=tf.keras.losses.sparse_categorical_crossentropy,
              metrics=['acc'])

model.fit(x_train, y_train, epochs=10, batch_size=100, verbose=2,
          validation_data=(x_test, y_test))
