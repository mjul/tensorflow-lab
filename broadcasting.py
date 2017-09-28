import tensorflow as tf
import numpy as np

sess = tf.Session()
sess.run(tf.global_variables_initializer())

a_2x3 = tf.constant([[1, 2, 3], [4, 5, 6]])
b_vec3 = tf.constant([10, 20, 30])

# This makes no sense mathematically
sum = a_2x3 + b_vec3

# In order to work around this, TensorFlow performs "broadcasting"
# turning the 3-vector into a matrix of two rows each with the elements
# of the 3-vector and applying the sum to that.

print(sess.run(sum, {}))

# [[11 22 33]
# [14 25 36]]

# Broadcasting with two matrices with different number of rows
# Like for the vector example above, the rows of the smaller one are replicated to the height of the other

b_1x3 = tf.constant([[10, 20, 30]])
print(sess.run(a_2x3 + b_1x3, {}))

# [[11 22 33]
# [14 25 36]]
