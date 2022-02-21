#!/usr/bin/env python
# coding: utf-8

# In[38]:


from helpers.labels import get_SpaceElementClasses, get_SpaceFunctionClasses
from sklearn.model_selection import train_test_split
import numpy as np
import tensorflow as tf
import cv2
import glob


# In[39]:


# to get all  Space Function Classes
SpaceFunctionClasses = get_SpaceFunctionClasses()

# to get the color of all  Space Function Classes
color_palette =[]
for key in SpaceFunctionClasses.keys():        
    color_palette.append(eval(SpaceFunctionClasses[key].color))
    
color_palette_np_array =   np.array(color_palette)


def read_transparent_png(filename):
    
    image_4channel = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    alpha_channel = image_4channel[:,:,3]
    rgb_channels = image_4channel[:,:,:3]

    # White Background Image
    white_background_image = np.ones_like(rgb_channels, dtype=np.uint8) * 255

    # Alpha factor
    alpha_factor = alpha_channel[:,:,np.newaxis].astype(np.float32) / 255.0
    alpha_factor = np.concatenate((alpha_factor,alpha_factor,alpha_factor), axis=2)

    # Transparent Image Rendered on White Background
    base = rgb_channels.astype(np.float32) * alpha_factor
    white = white_background_image.astype(np.float32) * (1 - alpha_factor)
    final_image = base + white
    
    return final_image.astype(np.uint8)


# In[40]:
def resize(input_image, label_image, height, width):
    input_image = tf.image.resize(input_image, [height, width],
                                method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)
    
    label_image = tf.image.resize(label_image, [height, width],
                               method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)
    
    return input_image, label_image

import matplotlib.image as mpimg



def load_input_mask_img(input_path, label_path,  height, width):

    inp_img = read_transparent_png(str(input_path).split("'")[1])
    inp_img = tf.cast(inp_img, tf.float32)
    inp_img = (inp_img / 127.5) - 1

    label = tf.io.read_file(label_path)
    label = tf.image.decode_png(label, 3)
    
    one_hot_map = []
    for color in color_palette_np_array:
        class_map = tf.reduce_all(tf.equal(label, color), axis=-1)
        one_hot_map.append(class_map)

    one_hot_map = tf.stack(one_hot_map, axis=-1)
    one_hot_map = tf.cast(one_hot_map, tf.float32)
    
    inp_img, one_hot_map  = resize(inp_img, one_hot_map, height, width)

    return inp_img, one_hot_map


# In[44]:


def load_dataset_path(dataset_path):
    
    space_function_paths = glob.glob(dataset_path + '/**/ground_truth/'+  '*.png', recursive=True)
    input_image_paths = glob.glob(dataset_path + '/**/input/'+ '*.png', recursive=True)

    dataset_paths  = { 'input_image_paths':input_image_paths, 'space_function_paths':space_function_paths}
    print(f"Number of input images: {len(dataset_paths['input_image_paths'])}" )
    print(f"Number of space function images: {len(dataset_paths['space_function_paths'])}" )

    return dataset_paths


# In[45]:


def create_training_test_dataset(dataset_path, test_size= 0.20, shuffle=True,  random_state=12):
    
    X_train, X_test, y_train, y_test = train_test_split(dataset_path['input_image_paths'],
                                                        dataset_path['space_function_paths'],
                                                        test_size= test_size, shuffle=shuffle,
                                                        random_state=random_state)
    
    print(f"Number of training data: {len(X_train)}" )
    print(f"Number of test data: {len(X_test)}" )
    
    return  X_train, y_train, X_test, y_test







