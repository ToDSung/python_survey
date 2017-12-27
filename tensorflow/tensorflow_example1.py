# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 23:59:46 2017

@author: wlunareve
"""

import tensorflow as tf
import numpy as np

'''
create data
'''
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1+0.3

'''
create tensorflow structure 
#weights 相當於 x_data*0.1 中的0.1 1維 初始值 -1 ~ 1
#biases  相當於 x_data*0.1+0.3 中的0.3
'''


weights = tf.Variable(tf.random_uniform([1],-1.0,1.0))
biases = tf.Variable(tf.zeros([1]))

y= weights*x_data+biases

#預測y 與實際y的差別
loss = tf.reduce_mean(tf.square(y-y_data))
#優化器 ， 選擇 GradientDescentOptimizer 優化器 數值通常小於1
optimizer=tf.train.GradientDescentOptimizer(0.5)
#減少誤差
train=optimizer.minimize(loss)

init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init) #Very important

for step in range(201):
    sess.run(train)
    if step% 20 == 0:
        print(step,sess.run(weights),sess.run(biases))
        