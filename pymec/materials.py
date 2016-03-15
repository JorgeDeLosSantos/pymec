# -*- coding: utf-8 -*-
# Materials
import numpy as np

class Material(object):
    def __init__(self,name,**kwargs):
        self.name = name
        if kwargs.has_key("E"): self.__E = kwargs["E"]
        if kwargs.has_key("nu"): self.__nu = kwargs["nu"]
    
    @property
    def nu(self):
        return self.__nu
        
    @nu.setter
    def nu(self,val):
        self.__nu = val
    
    @property
    def E(self):
        return self.__E
    
    @E.setter
    def E(self,val):
        self.__E = val


if __name__ == '__main__':
    m = Material("a", E=100, nu=0.3)
