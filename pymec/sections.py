# -*- coding: utf-8 -*-
# Sections 
import numpy as np


class Section(object):
    def __init__(self):
        pass
    
    def __str__(self):
        return "%s"%(self.__class__)

    
class RectangleSection(Section):
    def __init__(self,b,h):
        Section.__init__(self)
        self.b = b
        self.h = h
    
    @property
    def area(self):
        self.__area = self.b * self.h
        return self.__area
    
    @property
    def Ixx(self):
        self.__Ixx = ((self.b)*(self.h)**3)/12.0
        return self.__Ixx
        
    @property
    def Iyy(self):
        self.__Iyy = (((self.b)**3)*(self.h))/12.0
        return self.__Iyy
        

class CircularSection(Section):
    def __init__(self,r):
        Section.__init__(self)
        self.r = r
    
    @property
    def area(self):
        self.__area = np.pi*(self.r**2)
        return self.__area
    
    @property
    def Ixx(self):
        self.__Ixx = (np.pi/4.0)*self.r**4
        return self.__Ixx
        
    @property
    def Iyy(self):
        self.__Iyy = (np.pi/4.0)*self.r**4
        return self.__Iyy


class ISection(Section):
    def __init__(self,bw,bt,mw,mt,tw,tt):
        Section.__init__(self)
        self.bw = bw
        self.bt = bt
        self.mw = mw
        self.mt = mt
        self.tw = tw
        self.tt = tt
    
    @property
    def area(self):
        ab = self.bw*self.bt
        am = self.mw*self.mt
        at = self.tw*self.tt
        self.__area = ab + am + at
        return self.__area
    
    @property
    def Ixx(self):
        ixxb = ((self.bw*self.bt**3)/12.0) + (self.bw*self.bt)*(0.5*(self.tt+self.mw))**2
        ixxm = ((self.mt*self.mw**3)/12.0)
        ixxt = ((self.tw*self.tt**3)/12.0) + (self.tw*self.tt)*(0.5*(self.bt+self.mw))**2
        self.__Ixx = ixxb + ixxm + ixxt
        return self.__Ixx
        
    @property
    def Iyy(self):
        iyyb = ((self.bt*self.bw**3)/12.0)
        iyym = ((self.mw*self.mt**3)/12.0)
        iyyt = ((self.tt*self.tw**3)/12.0)
        self.__Iyy = iyyb + iyym + iyyt
        return self.__Iyy
        
    @property
    def centroid(self):
        ab = self.bw*self.bt
        yb = self.bt/2.0
        am = self.mw*self.mt
        ym = self.bt + self.mw/2.0
        at = self.tw*self.tt
        yt = self.bt + self.mw + self.tt/2.0
        yc = (ab*yb + am*ym + at*yt)/(ab + am + at)
        xc = self.bw/2.0
        return (xc, yc)


class TSection(Section):
    def __init__(self,mw,mt,tw,tt):
        Section.__init__(self)
        self.mw = mw
        self.mt = mt
        self.tw = tw
        self.tt = tt
    
    @property
    def area(self):
        am = self.mw*self.mt
        at = self.tw*self.tt
        self.__area = am + at
        return self.__area
    
    @property
    def Ixx(self):
        xc, yc = self.centroid
        ixxm = ((self.mt*self.mw**3)/12.0) + (self.mw*self.mt)*(yc-self.mw/2.0)**2
        ixxt = ((self.tw*self.tt**3)/12.0) + (self.tw*self.tt)*((self.mw+self.tt/2.0)-yc)**2
        self.__Ixx = ixxm + ixxt
        return self.__Ixx
        
    @property
    def Iyy(self):
        iyym = ((self.mw*self.mt**3)/12.0)
        iyyt = ((self.tt*self.tw**3)/12.0)
        self.__Iyy = iyym + iyyt
        return self.__Iyy
        
    @property
    def centroid(self):
        am = self.mw*self.mt
        ym = self.mw/2.0
        at = self.tw*self.tt
        yt = self.mw + self.tt/2.0
        yc = (am*ym + at*yt)/(am + at)
        xc = self.tw/2.0
        return (xc, yc)



if __name__ == '__main__':
    r = TSection(20,5,20,5)
    print r.area, r.centroid, r.Ixx, r.Iyy
