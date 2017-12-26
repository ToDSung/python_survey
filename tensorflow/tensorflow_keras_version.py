# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 00:10:26 2017

@author: wlunareve
"""

import tensorflow as tf
#import keras

#print(tf.__version__)
#print(keras.__version__)

hw =tf.constant("Hello World!")
with tf.Session() as sess:
    print(sess.run(hw))