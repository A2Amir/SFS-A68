#!/usr/bin/env python
# coding: utf-8

# In[1]:


from keras_unet_collection import models
from tensorflow.keras.utils import plot_model

# In[2]:



def get_unet_model(input_size = (320, 320, 3), n_labels= 22):
    
    unet_model = models.unet_2d(input_size, [64, 128, 256, 512], n_labels=n_labels,
                      stack_num_down=2, stack_num_up=2,
                      activation='LeakyReLU', output_activation='Sigmoid', 
                      batch_norm=True, pool=False , unpool=False, name='unet')
    return unet_model


# In[3]:


def get_vgg16_unet_model(input_size = (320, 320, 3), n_labels= 22):
    
    vgg_unet_model = models.unet_2d(input_size, [64, 128, 256, 512], n_labels=n_labels,
                                    stack_num_down=2, stack_num_up=2,
                                      activation='LeakyReLU', output_activation='Sigmoid', 
                                      backbone='VGG16', weights='imagenet', freeze_backbone=True,
                                      freeze_batch_norm=True, unpool=False, name='vgg16_unet')
    return vgg_unet_model
    


# In[4]:


if __name__=='__main__':
    
    unet_model = get_unet_model(input_size = (320, 320, 3), n_labels= 22)
    print(unet_model.summary())
    plot_model(unet_model, to_file='./unet_model.png',show_shapes=True, show_layer_names=True)
    
    vgg_unet_model = get_vgg16_unet_model(input_size = (320, 320, 3), n_labels= 22)
    print(vgg_unet_model.summary())
    plot_model(vgg_unet_model, to_file='./vgg_unet_model.png',show_shapes=True, show_layer_names=True)


# In[ ]:




