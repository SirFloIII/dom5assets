# -*- coding: utf-8 -*-
"""
Created on Sat May  7 21:22:27 2022

@author: Flo Strich
"""

scr_path = "..\dom5inspector\images\sprites"

dest_path = "sprites"

factor = 8

import os
import PIL
import numpy as np
from tqdm import tqdm

for file in tqdm(os.listdir(scr_path)):
    img = PIL.Image.open(os.path.join(scr_path, file))
    
    arr = np.array(img)
    
    arr[:,:,3] = (arr[:,:,3] > 0) * 255
    
    img = PIL.Image.fromarray(arr)
    
    img.resize([factor*s for s in img.size], PIL.Image.NEAREST).save(os.path.join(dest_path, file))