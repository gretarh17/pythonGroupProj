import pathlib
import re
import os
import shutil
def movie_filter(paths, destPath):
    try:
        os.makedirs(destPath+'/Movies/')
    except FileExistsError:
        pass
    for x in paths:
        if "sample" in x.lower():
            try:
                os.remove(x)
            except:
                pass
        newPath = destPath+'/Movies/'+'/'.join(x.split('\\')[1:])
        try:
            shutil.move(x,newPath)
        except:
            pass