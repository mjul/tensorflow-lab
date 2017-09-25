#
# Try some 'convolution' operations
# (mathematically speaking, they are not convolutions but cross-correlations)
#

import tensorflow as tf
import numpy as np

sess = tf.Session()
sess.run(tf.global_variables_initializer())

BATCH_SIZE = 1
HEIGHT = 4
WIDTH = 4
CHANNELS = 1

M = np.array([
    [[[1], [2], [3], [4]],
     [[0], [1], [2], [3]],
     [[0], [0], [1], [2]],
     [[0], [0], [0], [1]]]],
    dtype=np.float32)

filter_diagonal = np.array(
    [
        [[[1]], [[0]]],
        [[[0]], [[1]]]
    ],
    dtype=np.float32)

filter_vertical = np.array(
    [
        [[[1]], [[-1]]],
        [[[1]], [[-1]]]
    ],
    dtype=np.float32)


inputs_tf = tf.placeholder(tf.float32, shape=[BATCH_SIZE, HEIGHT, WIDTH, CHANNELS], name='input')
outputs_tf = [tf.nn.conv2d(inputs_tf, filter=f, strides=[1, 2, 1, 1], padding='SAME')
              for f in [filter_diagonal, filter_vertical]]

a, b = sess.run(outputs_tf, {inputs_tf: M})

print('conv2d with filters')
print('a (diag):', a)
print('b (vert):', b)

