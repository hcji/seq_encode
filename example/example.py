# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 10:20:36 2019

@author: hcji
"""

import os
import json
from tqdm import tqdm
from seq_encode.smiles import smiles_coder

with open('hmdb_smiles/hmdb_smiles.json', 'r') as js:
    hmdb_smiles = json.load(js)

coder = smiles_coder()
coder.fit(hmdb_smiles)
hot = coder.transform(hmdb_smiles)
rebuild = coder.inverse_transform(hot)

