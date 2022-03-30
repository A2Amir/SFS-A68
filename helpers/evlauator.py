#!/usr/bin/env python
# coding: utf-8

# In[38]:
import tensorflow as tf
from skimage.filters import threshold_otsu
import numpy as np

def iou_metric(inputs, target):
    intersection =  (target * inputs).sum()
    union = target.sum() + inputs.sum()
    if target.sum() == 0 and inputs.sum() == 0:
        return 1.0
    return intersection / union


def mIoU(prediction, ground_truth, threshold = .5):
    
    '''
    Intersection over union as a metric to quantify the quality of semantic segmentation
    
    Return:
    
        Mean IoU
        IoU for each class
        IoUs for each class
    '''
    
    assert (prediction.shape == ground_truth.shape)
    

    ious_per_class = []
    iou_per_class = []
    MIoU = 0.0

    for i in range(prediction.shape[-1]):
        ious = []
        for j in range(prediction.shape[0]):
            
            y_prediction = prediction[j,:,:,i]
            y_true = ground_truth[j,:,:,i]
            y_pred_class = tf.cast(y_prediction > threshold, tf.float32)
            ious.append(iou_metric(y_pred_class.numpy(), y_true.numpy()))

        ious_per_class.append(np.round(ious,2))
        iou_per_class.append(np.round(sum(ious)/len(ious),2))
    MIoU = sum(iou_per_class)/len(iou_per_class)
    
    return np.round(MIoU, 2), iou_per_class, ious_per_class