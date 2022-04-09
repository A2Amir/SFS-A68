#!/usr/bin/env python
# coding: utf-8

# In[38]:
import tensorflow as tf
import numpy as np
from keras import backend as K


def f_measure(prediction, ground_truth, smooth=1):
    
    '''
    F-Measure as a metric to quantify the quality of semantic segmentation
    
    Return:
    
        F-Measure for each class
        Mean F-Measure  fo all clasess
        
    '''
    assert (prediction.shape == ground_truth.shape)


    f_Measure = []
    mean_f_Measure = 0.0
    
    for i in range(prediction.shape[-1]):
        y_pred = prediction[:,:,:,i]
        y_true = ground_truth[:,:,:,i]
        
           
        true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
        possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
        recall = true_positives / (possible_positives + K.epsilon())
        
        predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
        precision = true_positives / (predicted_positives + K.epsilon())
        
        f_measure = 2*((precision*recall)/(precision+recall+K.epsilon())).numpy()
        f_Measure.append( np.round(f_measure, 2))
            
    mean_f_Measure = sum(f_Measure)/len(f_Measure)
    return  np.round(mean_f_Measure,2), f_Measure



def mIoU(prediction, ground_truth, threshold = 0.5, target_class_ids =[0,1]):
    
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
            m = tf.keras.metrics.BinaryIoU( target_class_ids= target_class_ids, threshold= threshold)            
            m.update_state(y_true, y_prediction)
            ious.append(m.result().numpy())
            
        ious_per_class.append(np.round(ious,2))
        iou_per_class.append(np.round(sum(ious)/len(ious),2))
    MIoU = sum(iou_per_class)/len(iou_per_class)
    
    return np.round(MIoU,2), iou_per_class, ious_per_class