"""
@author: George
"""
from jedd import Slide

def gen(v_photos):
    v_combo = list()
    for i in v_photos:
        for j in v_photos:
            if i.Id == j.Id:
                pass
            else:
                combo = [i, j]
                v_combo.append(Slide(combo))
    return v_combo
