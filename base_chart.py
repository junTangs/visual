import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class BaseChart:
    def __init__(self,**kwargs) -> None:
        self._draw_callback = None
        self.fig = None

    def set_draw_callback(self,cbk_fn):
        self._draw_callback = cbk_fn

    def draw(self,data,figsize = (3,3),ncols = 1, nrows = 1,legend = True,**kwargs):
        raise NotImplementedError

    def draw_ax(self,data,ax,legend,**kwargs):
        fontsize = kwargs.get("fontsize",15)
        if "xlabel" in kwargs:
            ax.set_xlabel(kwargs["xlabel"],fontsize)
        if "ylabel" in kwargs:
            ax.set_ylable(kwargs["ylabel"],fontsize)
        if "x_ticks" in kwargs:
            ax.set_xticks(*kwargs["x_ticks"])
        if "y_ticks" in kwargs:
            ax.set_xticks(*kwargs["y_ticks"])
        
        if legend:
            ax.legend(loc = 'best',fontsize = 15)
        if "title" in kwargs:
            ax.set_title(kwargs["title"])

        return ax
        

    def save(self,path,**kwargs):
        raise NotImplementedError