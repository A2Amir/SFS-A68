#!/usr/bin/env python
# coding: utf-8

# In[38]:

import tensorflow as tf





@tf.function
def inp_out_augmentation(x, y):
    """Random  Input and Output Augmentation.

    
      Args:
        input_image: Input Image
        output_image: Output Image
        Width should be equal with Height
        
      Returns:
        Input Image
        Output Image
    """


    if tf.random.uniform(()) > 0.2:
        
        # random mirroring
        x =  tf.image.flip_left_right(x)
        y =  tf.image.flip_left_right(y)

        
    if tf.random.uniform(()) > 0.2:
        
        # random mirroring
        x =  tf.image.flip_up_down(x)
        y =  tf.image.flip_up_down(y)
    
    
    if tf.random.uniform(()) > 0.2:
        
        # random counter clockwise by 90 degrees
        x =  tf.image.rot90(x)
        y =  tf.image.rot90(y)

    if tf.random.uniform(()) > 0.2:
        
        # random counter clockwise by 270 degrees
        x =  tf.image.rot90(x, k=3)
        y =  tf.image.rot90(y, k=3)
        
        
    if tf.random.uniform(()) > 0.2:
        # random_brightness
        x =  tf.image.random_brightness(x, 0.2)
    
    
    if tf.random.uniform(()) > 0.2:
        # transpose
        x =  tf.image.transpose(x)    
        y =  tf.image.transpose(y)

                
    return x,y