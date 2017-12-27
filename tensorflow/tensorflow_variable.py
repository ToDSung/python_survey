# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 15:52:14 2017

@author: wlunareve
"""

import tensorflow as tf

state = tf.Variable(0,name='counter')

print(state)

one = tf.constant(1)

newValue = tf.add(state , one)
update = tf.assign(state,newValue)
'''
must have if define variable
'''
init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)
for step in range(10):
    sess.run(update)
    print(sess.run(state))    