# -*- coding: utf-8 -*-
"""
Created on Sat May  7 23:33:55 2022

@author: Flo Strich
"""

scr_path = "..\dom5inspector\gamedata"

dest_file = "gamedata.lua"


import os
import pandas as pd
from tqdm import tqdm

with open(dest_file, "w") as f:
    
    for file in tqdm(os.listdir(scr_path)):
        if file[-3:] != "csv":
            f.write(f"{file} = {{\n")
            for subfile in os.listdir(os.path.join(scr_path, file)):
                with open(os.path.join(scr_path, file, subfile), 'r') as g:
                    index = subfile.replace(".txt", "").replace("-", "_")
                    if index.isdecimal():
                        index = "[" + index + "]"
                    f.write(f'{index} = "{g.readline().strip()}",\n')
            f.write("}\n")
        else:
            f.write(f"{file.replace('.csv', '')} = {{\n")
            df = pd.read_csv(os.path.join(scr_path, file),
                            sep = "\t")
            
            df.columns = [c.replace("-", "_").replace(".", "_") for c in df.columns]
            
            for i, x in df.iterrows():
                pre = f"[{x[0]}] = {{"
                entries = [f'''{df.columns[i+1]} = "{y.replace('"', "'") if isinstance(y, str) else y}"'''.encode("ascii", errors='ignore').decode("ascii") for i, y in enumerate(x[1:]) if str(y) != "nan"]
                end = "},\n"
                f.write(pre + ", ".join(entries) + end)
                
            f.write("}\n")
    