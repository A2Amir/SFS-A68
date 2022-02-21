#!/usr/bin/env python
# coding: utf-8

# In[38]:

from PIL import Image
from skimage import data
from skimage.filters import threshold_otsu
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import os


def visulaize_inp_pred_gt(inp_img, prediction, ground_truth,
                          img_height, img_width,
                          seg_classes, batch_n,
                          pred_path, save):
    
    """
     To visulaize input, ground truth and prediction based their colors
     
     Input
         inp_img: (batch, h, w, 3)
         prediction: (batch, h, w, number of space function classes)
         ground_truth: (batch, h, w, number of space function classes)
         seg_classes: Space Function Classes 
         batch_n: batch number to visualize
         pred_path: path to save prediction
         save: "True" means saving outputs in a RGB image and in channel format, "False" mean dont save.
              

    """
    
    # to visulaize input, ground truth and prediczion based their colors
    
    gt_rgb = np.zeros((img_height, img_width,3), dtype=np.uint8)
    pred_rgb = np.zeros((img_height, img_width,3), dtype=np.uint8)
    pred_chs = []
    ground_truth_chs = []


    for i,item in seg_classes.items():
        
        pred_ch = np.zeros((img_height, img_width,1), dtype=np.uint8)
        gr_truth_ch = np.zeros((img_height, img_width,1), dtype=np.uint8)

        # Threshold image to binary
        pred_image = prediction [batch_n][:,:,item.id-1]
        pred_thresh = threshold_otsu(pred_image)
        pred_binary = pred_image > pred_thresh
        pred_rgb[pred_binary]  = eval(item.color)
        
        pred_ch[pred_binary]  = 1
        pred_chs.append(pred_ch)

        gt_image = np.array(ground_truth[batch_n][:,:,item.id-1])
        gt_thresh = threshold_otsu(gt_image)
        gt_binary = gt_image > gt_thresh
        gt_rgb[gt_binary]  = eval(item.color)
        
        gr_truth_ch[gt_binary]  = 1
        ground_truth_chs.append(gr_truth_ch)
        
    # Display result
    plt.figure(figsize=(18,18))
    display_list = [inp_img[batch_n,:,:,:]*.5+.5, gt_rgb, pred_rgb]
    display_title = ['Input Image', 'Ground Truth', 'Predction']

    for i in range(3):
        plt.subplot(1, 3, i+1)
        plt.title(display_title[i])
        plt.imshow(display_list[i] )
        plt.axis('off')
    plt.show()

    if save:
        ch_path = pred_path  +'/' +  str(batch_n+1)
        if not os.path.exists(ch_path):
            os.makedirs(ch_path)
        
        
        inp  = (inp_img[batch_n,:,:,:].numpy() * 255).astype(np.uint8)
        gt_rgb = (gt_rgb).astype(np.uint8) 
        pred_rgb = (pred_rgb).astype(np.uint8) 
        save_image = np.hstack((inp ,gt_rgb, pred_rgb))

        tf.keras.utils.save_img(ch_path +'/' + 'rgb_input_groundTruth_pred' +'.jpg', save_image)

        
        tf.keras.utils.save_img(ch_path +'/' + 'inp_image' + '.jpg', inp_img[batch_n,:,:,:]*.5+.5)
        for i in range (len(seg_classes)):
            plot_image = np.concatenate((ground_truth_chs[i], pred_chs[i]), axis=1)
            tf.keras.utils.save_img(ch_path +'/' + 'gt_pred_chanel'  + '_' + str(i+1) +'.jpg', plot_image)

    