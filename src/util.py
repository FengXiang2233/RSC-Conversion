import logging
import shutil  
import os

def clean(path:str):
    if os.path.exists(path):
        shutil.rmtree(path)
        logging.debug(f"{path} 已清理")
    else:
        logging.debug(f"{path} 不存在")
    os.mkdir(path)

def copy(path, topath):  
    if not os.path.exists(topath):  
        os.makedirs(topath)    
    for item in os.listdir(path):  
        p = os.path.join(path, item)  
        to = os.path.join(topath, item)   
        if os.path.isdir(p):  
            copy(p, to) 
        else:  
            shutil.copy2(p, to)  