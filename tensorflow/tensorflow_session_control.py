# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 14:53:47 2017

@author: wlunareve
"""

import tensorflow as tf
'''
注意Session控制 ， 必須先建立好神經結構 ， 在開啟Session 執行操作
'''

'''
double dimension tensor
'''

# 1 * 2 的矩陣
matrix1 = tf.constant([[3,3]])
# 2 * 1 的矩陣
matrix2 = tf.constant([[2],[2]])
# matmul 相乘
product1 = tf.matmul(matrix1,matrix2)

sess = tf.Session()
print(sess.run(matrix1))
print(sess.run(matrix2))
print(sess.run(product1))

sess.close()

'''
triple dimension tensor
'''
matrix3=tf.constant(np.arange(1,13), shape=[2, 2, 3])
matrix4=tf.constant(np.arange(13,25),shape=[2, 3, 2]) 

product2=tf.matmul(matrix3,matrix4)

sess = tf.Session()
print(sess.run(matrix3))
print(sess.run(matrix4))
print(sess.run(product2))

sess.close()