# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 10:20:36 2019

@author: hcji
"""

import os
import json
from tqdm import tqdm
from smiles_to_onehot.encoding import get_dict, one_hot_coding

with open('hmdb_smiles/hmdb_smiles.json', 'r') as js:
    hmdb_smiles = json.load(js)
    
words = get_dict(hmdb_smiles, save_path=os.getcwd())

x = []
for smi in tqdm(hmdb_smiles):
    xi = one_hot_coding(smi, words, max_len=100)
    x.append(xi)