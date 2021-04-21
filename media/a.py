x = tf.Variable(np.array([[1, 1.2, 1.3],[1, 1.5, 1.2]]), dtype = tf.float32)

z = tf.Variable(np.array([[1, 1],[1.2, 1.2], [2, 1.7]]), dtype = tf.float32)

y = tf.matmul(x, z)

g = tf.gradients(y, x)

init = tf.global_variables_initializer()

sess = tf.Sessionsess.run([init])

out = sess.run(g)
