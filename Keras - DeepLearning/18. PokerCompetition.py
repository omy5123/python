import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn import preprocessing, model_selection

# poker-hand 데이터셋을 추가하지 않았기 때문에 동작 x

# 1번. 스케일링
def apply_scaling(x):
    return preprocessing.scale(x)

# 2번. 원핫 벡터 사용
def apply_onehot(x):
    # suit: 4가지 * 5 = 20
    # card: 13가지 * 5 = 65
    enc = preprocessing.LabelBinarizer() # 인코더를 만듬

    binds = []
    for i in range(x.shape[1]):
        binds.append(enc.fit_transform(x[:,i]))
        # print(binds[-1].shape)

    return np.hstack(binds)

# 3번. 정렬(원본 순서 유지)
def apply_sort_1(x):
    print(x[0])         # [ 2 10  1  4  3 10  1 10  2 11]
    x = [np.reshape(i, [5, 2]) for i in x]
    print(x[0])         # [[ 2 10] [ 1  4] [ 3 10] [ 1 10] [ 2 11]]
    x = [sorted(i, key=lambda t:t[1]) for i in x]
    print(x[0])
    x = [np.reshape(i, (-1)) for i in x]
    print(x[0])         # [ 1  4  2 10  3 10  1 10  2 11]
    return np.int32(x)

# 4번. 정렬(숫자를 앞에, 무늬를 뒤에)
def apply_sort_2(x):
    cards = x[:, 1::2]      # 1 3 5 7 9
    suits = x[:, 0::2]      # 0 2 4 6 8
    cards.sort()
    return np.hstack([cards, suits])

# 5번. 피처 추가
def apply_feature(x):
    # flush 피처(bool)
    suits = [(r[0] == r[2] and (r[0] == r[4]) and (r[0] == r[6]) and (r[0] == r[8])) for r in x]

    # strait 피처(bool)
    straits = []
    for r in x:
        d = sorted(r[1::2])
        straits.append(d[0]+1 == d[1] and d[0]+2 == d[2] and d[0]+3 == d[3] and d[0]+4 == d[4])

    return np.hstack([x, np.transpose([suits, straits])])

poker = pd.read_csv('data/train.csv', index_col=0)

x = poker.values[:, :-1]
y = poker.values[:, -1:]

# x = apply_scaling(x)  # 대단한 효과
# x = apply_onehot(x)      # (25010, 85)
# x = apply_sort_1(x)
x = apply_sort_2(x)
# x = apply_feature(x)       # (25010, 12)

x_train, x_valid, y_train, y_valid = model_selection.train_test_split(x, y, train_size=0.8)

model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.layers.Dense(10, activation='softmax'))

model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.01),
              loss=tf.keras.losses.sparse_categorical_crossentropy,
              metrics=['acc'])

model.fit(x_train, y_train,
          epochs=100, batch_size=100, verbose=2,
          validation_data=(x_valid, y_valid))

# baseline_model : val_loss: 0.5620 - val_acc: 0.7867
# scale : val_loss: 0.0240 - val_acc: 0.9974
# onehot : val_loss: 0.1530 - val_acc: 0.9932
# sort 1 : val_loss: 0.3670 - val_acc: 0.9964
# sort 2 : val_loss: 0.0202 - val_acc: 0.9956
# feature : val_loss: 0.6620 - val_acc: 0.7681