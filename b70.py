"""
@author: George
"""
from jedd import Slide


def gen(v_photos):
    v_combo = list()
    for i in range(0, len(v_photos)):
        x = v_photos[i]
        for j in range(i+1, len(v_photos)):
            y = v_photos[j]
            combo = [x, y]
            v_combo.append(Slide(combo))
    return v_combo
