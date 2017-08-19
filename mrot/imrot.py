# -*- coding: utf-8 -*-
"""
@author: R. Patrick Xian
"""

from math import cos, sin, radians
import numpy as np

class Rotator(object):
    
    def __init__(self, img):
        self.img = img
        self.nrow, self.ncol = np.shape(img)
        self.rotimg = img
    
    
    @property
    def indices(self):
        return np.meshgrid(range(self.nrow), range(self.ncol))
    
    
    @staticmethod
    def rotmatrix(angle_deg):
        
        angle_rad = radians(angle_deg)
        rotationMatrix = np.array([[cos(angle_rad), -sin(angle_rad)],
                                   [sin(angle_rad), cos(angle_rad)]])
        return rotationMatrix
    
    
    def rotate(self, angle, origin=(0, 0)):
        
        rows, cols = self.indices
        rows_shifted = rows - origin[0]
        cols_shifted = cols - origin[1]
        imgrotated = np.zeros(self.img.shape)
        
        for r, c, rsh, csh in np.nditer([rows, cols, rows_shifted, cols_shifted]):
            rotr, rotc = np.round(self.rotmatrix(angle).dot([rsh, csh])).astype('int')
            rotr = rotr + origin[0]
            rotc = rotc + origin[1]
            if rotr>=0 and rotr<self.nrow and rotc>=0 and rotc<self.ncol:
                imgrotated[rotr, rotc] = self.img[r, c]
        
        self.rotimg = imgrotated