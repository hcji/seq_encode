# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 10:14:33 2019

@author: hcji
"""

import numpy as np
from tqdm import tqdm


class smiles_coder:
    
    def __init__(self):
        self.char_set = set([' '])
        self.char_to_int = None
        self.int_to_char = None
        self.fitted = False
        
    def fit(self, smiles_data, max_length = 150):
        for i in tqdm(range(len(smiles_data))):
            smiles_data[i] = smiles_data[i].ljust(max_length)
            self.char_set = self.char_set.union(set(smiles_data[i]))
        self.max_length = max_length
        self.n_class = len(self.char_set)
        self.char_to_int = dict((c, i) for i, c in enumerate(self.char_set))
        self.int_to_char = dict((i, c) for i, c in enumerate(self.char_set))
        self.fitted = True
        
    def transform(self, smiles_data):
        if not self.fitted:
            raise ValueError('smiles coder is not fitted')
        m = []
        for i in tqdm(range(len(smiles_data))):
            smiles_data[i] = smiles_data[i].ljust(self.max_length)
            chars = smiles_data[i]
            l = np.zeros((self.max_length, self.n_class))
            for t, char in enumerate(chars):
                if t >= self.max_length:
                    break
                else:
                    if char in self.char_set:
                        l[t, self.char_to_int[char]] = 1
            m.append(l)
        return np.array(m)
        
    def label(self, smiles_data):
        if not self.fitted:
            raise ValueError('smiles coder is not fitted')
        m = []
        for i in tqdm(range(len(smiles_data))):
            smiles_data[i] = smiles_data[i].ljust(self.max_length)
            chars = smiles_data[i]
            l = np.zeros((self.max_length, 1))
            for t, char in enumerate(chars):
                if t >= self.max_length:
                    break
                else:
                    if char in self.char_set:
                        l[t, 0] = self.char_to_int[char]
            m.append(l)
        return np.array(m)
    
    def inverse_transform(self, m):
        if not self.fitted:
            raise ValueError('smiles coder is not fitted')
        smiles_out = []
        for l in m:
            ll = np.argmax(l, axis=1)
            string = ''
            for t in ll:
                if self.int_to_char[t] == ' ':
                    continue
                string += self.int_to_char[t]
            smiles_out.append(string)
        return np.array(smiles_out)
    
    def inverse_label(self, l):
        if not self.fitted:
            raise ValueError('smiles coder is not fitted')
        smiles_out = []
        for ll in l:
            string = ''
            for t in ll:
                if self.int_to_char[t] == ' ':
                    continue
                string += self.int_to_char[t]
            smiles_out.append(string)
        return np.array(smiles_out)

    def int_to_char(self):
        return self.int_to_char
    
    def char_to_int(self):
        return self.char_to_int

    def save(self, save_path):
        np.savez(save_path, char_set = self.char_set, char_to_int=self.char_to_int, int_to_char=self.int_to_char,
                            max_length = self.max_length, n_class = len(self.char_set))
        
    def load(self, save_path):
        saved = np.load(save_path, allow_pickle=True)
        self.char_set = saved['char_set'].tolist()
        self.char_to_int = saved['char_to_int'].tolist()
        self.int_to_char = saved['int_to_char'].tolist()
        self.max_length = saved['max_length'].tolist()
        self.n_class = len(self.char_set)
        self.fitted = True
        