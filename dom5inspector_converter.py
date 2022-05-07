# -*- coding: utf-8 -*-
"""
Created on Sat May  7 21:22:27 2022

@author: Flo Strich
"""

scr_path = "..\dom5inspector\images\sprites"

dest_path = "sprites"

factor = 5

import os
import PIL
from tqdm import tqdm

for file in tqdm(os.listdir(scr_path)):
    img = PIL.Image.open(os.path.join(scr_path, file))
    
    img.resize([factor*s for s in img.size], PIL.Image.NEAREST).save(os.path.join(dest_path, file))