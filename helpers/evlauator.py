#!/usr/bin/env python
# coding: utf-8

# In[38]:
import tensorflow as tf
import numpy as np
from keras import backend as K


def total_error(prediction, ground_truth):
    
    '''
    Total error a metric to quantify the quality of semantic segmentation
    
             (FN+FP)/(FP+TP+TN+FN) 
    
    Return:
    
        Mean Total error
        Total error for each class
        Total errors for each class
    '''
    
    ground_truth = ground_truth.numpy()
    assert (prediction.shape == ground_truth.shape)

    total_errors_per_class = []
    total_error_per_class = []
    Mtotal_error = 0.0

    for i in range(ground_truth.shape[-1]):
        total_errors = []
        for j in range(ground_truth.shape[0]):

            y_pred = prediction[j,:,:,i]
            y_true = ground_truth[j,:,:,i]

            y_pred = (y_pred > 0.5)

            y_pred = y_pred.ravel()
            y_true = y_true.ravel()

            # True Positive (TP): we predict a label of 1 (positive), and the true label is 1.
            TP = np.sum(np.logical_and(y_pred == 1, y_true == 1))  # True Negative (TN): we predict a label of 0 (negative), and the true label is 0.
            TN = np.sum(np.logical_and(y_pred == 0, y_true == 0))  # False Positive (FP): we predict a label of 1 (positive), but the true label is 0.
            FP = np.sum(np.logical_and(y_pred == 1, y_true == 0))  # False Negative (FN): we predict a label of 0 (negative), but the true label is 1.
            FN = np.sum(np.logical_and(y_pred == 0, y_true == 1)) 

            total_error = (FN+FP)/(FP+TP+TN+FN)
            total_errors.append( total_error)

        total_errors_per_class.append(np.round(total_errors,3))
        total_error_per_class.append(np.round(sum(total_errors)/len(total_errors),3))
    Mtotal_error = sum(total_error_per_class) / len(total_error_per_class)
    
    return np.round(Mtotal_error, 3), total_error_per_class, total_errors_per_class
    


def f1_measure(prediction, ground_truth, smooth=1):
    
    '''
    F1-Measure as a metric to quantify the quality of semantic segmentation
    
    Return:
    
        F-Measure for each class
        Mean F-Measure  fo all clasess
        
    '''
    assert (prediction.shape == ground_truth.shape)


    f1_Measure = []
    mean_f1_Measure = 0.0
    
    for i in range(prediction.shape[-1]):
        y_pred = prediction[:,:,:,i]
        y_true = ground_truth[:,:,:,i]
        
           
        true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
        possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
        recall = true_positives / (possible_positives + K.epsilon())
        
        predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
        precision = true_positives / (predicted_positives + K.epsilon())
        
        f1_measure = 2*((precision*recall)/(precision+recall+K.epsilon())).numpy()
        f1_Measure.append( np.round(f1_measure, 2))
            
    mean_f1_Measure = sum(f1_Measure)/len(f1_Measure)
    return  np.round(mean_f1_Measure,2), f1_Measure



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