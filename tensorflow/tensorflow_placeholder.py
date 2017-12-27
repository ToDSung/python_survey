# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 20:14:20 2017

@author: wlunareve
"""

import tensorflow as tf

'''
placeholder funtion 用法暫時儲存變數
使用feed_dict={} 來賦值
'''
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)

output = tf.multiply(input1,input2)

sess=tf.Session()

print(sess.run(output,feed_dict={input1 : [7.], input2 : [2.]}))