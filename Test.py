import tensorflow as tf

a = tf.constant([1.0, 2.0, 3.0], name="a")
b = tf.constant([5.0, 6.0, 7.0], name="b")
result = a + b

print(result)

sess = tf.InteractiveSession()
print(result.eval())

