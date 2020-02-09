# 用户登陆
# 注册
# 密码找回
# 登陆的验证
# 修改和注册的验证
# 访问记录，日后添加
# Python
# import tensorflow as tf
# import tensorflow.compat.v1 as tf
# tf.disable_v2_behavior()
# hello = tf.constant('Hello, TensorFlow!')
# sess = tf.Session()
# print(sess.run(hello))
import tensorflow as tf
tf.compat.v1.disable_eager_execution()
hello = tf.constant('Hello, TensorFlow!')
sess = tf.compat.v1.Session()
print(sess.run(hello))
