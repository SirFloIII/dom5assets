# -*- coding: utf-8 -*-
"""
Created on Sun May  8 02:26:06 2022

@author: Flo Strich
"""

scr_path = "..\dom5inspector\images\sprites"

dest_file = "unit_size.lua"


import os
import PIL
from tqdm import tqdm



with open(dest_file, "w") as f:
    
    f.write("unit_size = {\n")

    for file in tqdm(os.listdir(scr_path)):
        if "_2" in file:
            continue
        img = PIL.Image.open(os.path.join(scr_path, file))
        n = int(file.replace("_1.png", ""))
        f.write(f"[{n}] = {{w = {img.size[0]}, h = {img.size[1]}}},\n")
        
 
    f.write("}\n")