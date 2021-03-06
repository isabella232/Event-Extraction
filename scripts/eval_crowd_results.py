#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 11:39:03 2018

@author: oanainel
"""

import os


def compute_P(tp, fp):
    if tp == 0:
        return 0
    return float(tp) / float(tp + fp)


def compute_R(tp, fn):
    if tp == 0:
        return 0
    return float(tp) / float(tp + fn)

def compute_A(tp, tn, fp, fn):
    if tp + tn == 0:
        return 0
    return float(tp + tn) / float(tp + tn + fp + fn)

def compute_F1(p, r):
    if p * r == 0:
        return 0
    return float(2 * p * r) / float(p + r)
    


def compute_crowd_performance(crowd_results, crowd_score):
    rows = []
    header = ["Thresh", "TP", "TN", "FP", "FN", "Precision", "Recall", "Accuracy", "F1-score"]
    rows.append(header)
    
    for i in range(5, 101, 5):
        row = []
        thresh = i / 100.0
                    
        tp = 0
        tn = 0
        fp = 0
        fn = 0
        
        for j in range(len(crowd_results.index)):
            
            if crowd_results[crowd_score].iloc[j] >= thresh:
                if crowd_results["Experts"].iloc[j] == 1:
                    tp = tp + 1
                else:
                    fp = fp + 1
            else:
                if crowd_results["Experts"].iloc[j] == 1:
                    fn = fn + 1
                else:
                    tn = tn + 1
    
        p = compute_P(tp, fp)
        r = compute_R(tp, fn)
        a = compute_A(tp, tn, fp, fn)
        f1 = compute_F1(p, r)
        
        row = [thresh, tp, tn, fp, fn, p, r, a, f1]
        rows.append(row)
        
    return rows

