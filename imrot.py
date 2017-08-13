# -*- coding: utf-8 -*-
"""
@author: R. Patrick Xian
"""

from math import cos, sin, radians
import numpy as np

class Rotator:
    
    def __init__(self, img):
        self.img = img
        self.nr, self.nc = np.shape(img)
        self.rowind, self.colind = np.meshgrid(range(self.nr), range(self.nc))
        self.rotimg = np.zeros((self.nr, self.nc))
        
    def _rotmatrix(self, angle_deg):
        
        angle_rad = radians(angle_deg)
        rotationMatrix = np.array([[cos(angle_rad), -sin(angle_rad)],
                                   [sin(angle_rad), cos(angle_rad)]])
        
        return rotationMatrix
    
    def rotate(self, angle):
        
        for r in range(self.nr):
            for c in range(self.nc):
                rotr, rotc = np.round(self._rotmatrix(angle).dot([r, c])).astype('int')
                if rotr>=0 and rotr<self.nr and rotc>=0 and rotc<self.nc: 
                    self.rotimg[rotr, rotc] = self.img[r, c]