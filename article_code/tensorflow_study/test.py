import tensorflow
from tensorflow import keras

model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')

import numpy as np

# 建立并编译模型.
# model = keras.Sequential()
# model.add(keras.layers.Dense(units=1, input_shape=[1]))
# model.compile(optimizer='sgd', loss='mean_squared_error')

# 生成一些用于训练的数据.
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

# 用 fit() 训练模型.
model.fit(xs, ys, epochs=500)
print(model.predict([10.0]))
# 用 predict() 推理.
# print(model.predict(np.array([[5]])))
