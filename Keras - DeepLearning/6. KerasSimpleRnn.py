# sample이 좋지않음 (시계열에 대한)

import tensorflow as tf
import numpy as np

np.set_printoptions(precision=2) #소수점의 갯수

# 문제
# 아래와 같은 형태의 데이터를 7개만 만들어 주세요 (x, y 반환)
# [0.1, 0.2, 0.3, 0.4]  0.5
# [0.2, 0.3, 0.4, 0.5]  0.6
# [0.3, 0.4, 0.5, 0.6]  0.7

# 문제
# 아래에서 생성한 데이터에 대해 예측하세요.
def get_data():
    x, y = [], []
    for i in np.arange(0.1, 0.8, 0.1):
        x.append([i, i+0.1, i+0.2, i+0.3])
        y.append(i + 0.4)

    # print(x)
    # print(y)

    # broadcast 연산 적용
    # a = np.float32([0.1, 0.2, 0.3, 0.4])
    # b = np.arange(0, 1, 0.1).reshape(-1,1)
    # print(a + b)"""  # 위에 데이터를 만드는것 보다 잘안쓸거같다.

    # rnn 검증을 위해 3차원으로 변환
    return np.float32([x]), np.float32([y])

def simple_regression():
    x, y = get_data()
    print(x.shape, y.shape)

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(1))

    model.compile(optimizer=tf.keras.optimizers.SGD(),
                  loss=tf.keras.losses.mse)

    model.fit(x,y,epochs=100, verbose=0)
    print(model.evaluate(x,y))

    preds = model.predict(x).reshape(-1)

    print(preds)
    print(y)
    print(preds - y)

simple_regression()

def simple_rnn():
    x, y = get_data()
    print(x.shape, y.shape)

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.SimpleRNN(7, return_sequences=True))
    model.add(tf.keras.layers.Dense(1))

    model.compile(optimizer=tf.keras.optimizers.SGD(),
                  loss=tf.keras.losses.mse)

    model.fit(x, y, epochs=100, verbose=0)
    # print(model.evaluate(x, y, verbose=0))

    preds = model.predict(x).reshape(-1)
    y = y.reshape(-1)
    print(preds)
    print(y)
    print(preds - y)

simple_rnn()