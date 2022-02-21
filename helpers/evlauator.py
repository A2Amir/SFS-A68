#!/usr/bin/env python
# coding: utf-8

# In[38]:

from skimage.filters import threshold_otsu
from sklearn.metrics import jaccard_score
import numpy as np


def mIoU(prediction, ground_truth):
    
    '''
    Intersection over union as a metric to quantify the quality of semantic segmentation
    
    Return:
    
        Mean IoU
        IoU for each class
    '''
    
    assert (prediction.shape == ground_truth.shape)
    

    labels = [0, 1]
    Jaccards = []

    for b in range(prediction.shape[0]):
        jaccards = []
        for ch in range(prediction.shape[3]):

            pred_image = prediction [b][:,:,ch]
            pred_thresh = threshold_otsu(pred_image)
            pred_binary = pred_image > pred_thresh


            gt_image = ground_truth[b][:,:,ch]
            gt_thresh = threshold_otsu(gt_image)
            gt_binary = gt_image > gt_thresh

            jaccard = []
            for label in labels:
                jaccard.append(jaccard_score(gt_binary.flatten(),pred_binary.flatten(), pos_label=label))
            jaccards.append(jaccard)

        Jaccards.append(jaccards)
            #print(pred_binary.shape)
            #plt.imshow(pred_binary, cmap='gray')
            #plt.show()

    Jaccards = np.array(Jaccards)
    miou = np.round(np.mean(Jaccards, axis=2).mean(axis=0).mean(), 2)
    ious = np.round(np.mean(Jaccards, axis=2).mean(axis=0), 2)
    return miou,ious