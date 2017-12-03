import tensorflow as tf

a = tf.constant(3.9)
b = tf.constant(4.2)

c = tf.multiply(a,b)
sess = tf.Session()

print (sess.run(c))	
