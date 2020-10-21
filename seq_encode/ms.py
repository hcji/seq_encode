# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 09:26:10 2020

@author: jihon
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import sparse

data = np.vstack([[33,3], [44,2], [[55,1]]])

class ms_to_vec:
    
    def __init__(self, precision = 0.1, max_mz = 1000, reverse = False):
        self.precision = precision
        self.max_mz = max_mz
        self.reverse = reverse
        
    def transform(self, data, sparse_vec = False, precursor=None):
        self.precursor = precursor
        data = data[data[:,0] < self.max_mz,:]
        length = int(self.max_mz * 1 / self.precision)
        if not self.reverse:
            index = (data[:,0]  * 1 / self.precision).astype(int)
        else:
            data = data[data[:,0] < self.precursor,:]
            index = ((self.precursor - data[:,0])  * 1 / self.precision).astype(int)
            
        value = data[:,1] / np.max(data[:,1])
        vector = np.zeros(length)
        vector[index] = value
        if sparse_vec:
            return sparse.csr_matrix(vector)
        else:
            return vector
            
    def inverse_transform(self, vector):
        index = np.where(vector > 0)[0]
        if not self.reverse:
            mz = index * self.precision
        else:
            mz = self.precursor - index * self.precision
            
        value = vector[index]
        data = np.vstack((mz, value)).transpose()
        return np.sort(data, axis = 0)
    
       