# TensorFlow

## 安装

在 Anaconda 中，你可以使用 conda 来创建虚拟环境。但是，在 Anaconda 中，我们建议使用 `pip install` 而不是 `conda install` 命令来安装 TensorFlow。

```python
pip install tensorflow
```

使用上述命令安装即可，若出现错误，请查阅相关资料。

测试安装成功：

```python
import tensorflow as tf
tf.compat.v1.disable_eager_execution()
hello = tf.constant('Hello, TensorFlow!')
sess = tf.compat.v1.Session()
print(sess.run(hello))
```

如果系统正确的输出了下面的内容，那么说明你已经正确安装了 TensorFlow：

`b'Hello, TensorFlow!'`

若运行出现错误，请查阅相关资料。

