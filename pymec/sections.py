# -*- coding: utf-8 -*-
# Sections 
import numpy as np
import matplotlib.pyplot as plt

class Section(object):
    def __init__(self):
        pass
    
    def __str__(self):
        return "%s"%(self.__class__)

    
class RectangularSection(Section):
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
        
    @property
    def centroid(self):
        return (self.b/2.0, self.h/2.0)
        
    def plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        xc,yc = self.centroid
        xx = [0, self.b, self.b, 0]
        yy = [0, 0, self.h, self.h]
        ax.fill(xx, yy, color=(0,0,1,0.3))
        ax.plot(xc, yc, "rx")
        kb, kh = self.b/10.0, self.h/10.0
        ax.set_xlim(-kb, self.b + kb)
        ax.set_ylim(-kh, self.h + kh)
        plt.show()
        
        

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
        
    @property
    def centroid(self):
        return (self.r, self.r)
        
    def plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        xc,yc = self.centroid
        t = np.linspace(0,2*np.pi,100)
        xx = self.r*np.cos(t) + self.r
        yy = self.r*np.sin(t) + self.r
        ax.fill(xx, yy, color=(0,0,1,0.3))
        ax.plot(xc, yc, "rx")
        kb, kh = self.r/10.0, self.r/10.0
        ax.set_xlim(-kb, 2*self.r + kb)
        ax.set_ylim(-kh, 2*self.r + kh)
        ax.set_aspect('equal')
        plt.show()



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

    def plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        xc,yc = self.centroid
        xx1 = [0,self.bw,self.bw,0]
        yy1 = [0,0,self.bt,self.bt]
        xx2 = [xc-self.mt/2.0,xc+self.mt/2.0,xc+self.mt/2.0,xc-self.mt/2.0]
        yy2 = [self.bt,self.bt,self.bt+self.mw,self.bt+self.mw]
        xx3 = [xc-self.tw/2.0,xc+self.tw/2.0,xc+self.tw/2.0,xc-self.tw/2.0]
        yy3 = [self.bt+self.mw,self.bt+self.mw,self.bt+self.mw+self.tt,self.bt+self.mw+self.tt]
        ax.fill(xx1, yy1, color=(0,0,1,0.4))
        ax.fill(xx2, yy2, color=(0,0,1,0.4))
        ax.fill(xx3, yy3, color=(0,0,1,0.4))
        ax.axhline(y=yc, ls="dotted", color="r")
        ax.axvline(x=xc, ls="dotted", color="r")
        ax.plot(xc, yc, "rx")
        ax.text(xc+xc/50.0, yc+yc/50.0, "(%0.2f, %0.2f)"%(xc,yc))
        kb, kh = self.bw/10.0, (self.bt + self.mw + self.tt)/10.0
        ax.set_xlim(-kb, 10*kb + kb)
        ax.set_ylim(-kh, 10*kh + kh)
        ax.grid()
        ax.set_aspect("equal")
        plt.show()


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

    def plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        xc,yc = self.centroid
        xx1 = [xc-self.mt/2.0,xc+self.mt/2.0,xc+self.mt/2.0,xc-self.mt/2.0]
        yy1 = [0,0,self.mw,self.mw]
        xx2 = [xc-self.tw/2.0,xc+self.tw/2.0,xc+self.tw/2.0,xc-self.tw/2.0]
        yy2 = [self.mw,self.mw,self.mw+self.tt,self.mw+self.tt]
        ax.fill(xx1, yy1, color=(0,0,1,0.4))
        ax.fill(xx2, yy2, color=(0,0,1,0.4))
        ax.axhline(y=yc, ls="dotted", color="r")
        ax.axvline(x=xc, ls="dotted", color="r")
        ax.plot(xc, yc, "rx")
        ax.text(xc+xc/50.0, yc+yc/50.0, "(%0.2f, %0.2f)"%(xc,yc))
        kb, kh = self.tw/10.0, (self.mw + self.tt)/10.0
        ax.set_xlim(-kb, 10*kb + kb)
        ax.set_ylim(-kh, 10*kh + kh)
        ax.grid()
        ax.set_aspect("equal")
        plt.show()
        
        
class FunctionSection(Section):
    def __init__(self,fx,a,b):
        Section.__init__(self)
        self.fx = fx
        self.a = a
        self.b = b
    
    @property
    def area(self):
        x = np.linspace(self.a, self.b)
        y = eval(self.fx)
        self.__area = np.trapz(y, x)
        return self.__area



if __name__ == '__main__':
    r = FunctionSection("x",0,5)
    print r.area
