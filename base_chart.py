import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

import pandas as pd
import numpy as np


class BaseChart:
    def __init__(self,**kwargs) -> None:
        self._draw_callback = None
        self.fig = None

    def set_draw_callback(self,cbk_fn):
        self._draw_callback = cbk_fn

    def draw(self,data,style,figsize = (3,3),legend = True,**kwargs):
        
        with plt.style.context(style):
            self.fig, ax = plt.subplots(ncols=1,nrows=1,figsize = figsize)

            self.draw_ax(data,ax,legend, **kwargs)
            
            if self._draw_callback is not None:
                self._draw_callback(self.fig,ax,data)
            return 

    def draw_ax(self,data,ax,legend,**kwargs):
        fontsize = kwargs.get('fontsize',15)
        if 'font' in kwargs:
            font = fm.FontProperties(fname= kwargs['font'],size = fontsize)
        else:
            font = fm.FontProperties(fname= 'visual/font/Times New Roman.ttf',size = fontsize)

        if "xlabel" in kwargs:
            ax.set_xlabel(kwargs['xlabel'],fontproperties = font)
        if "ylabel" in kwargs:
            ax.set_ylabel(kwargs["ylabel"],fontproperties = font)
        if "x_ticks" in kwargs:
            ax.set_xticks(kwargs["x_ticks"],fontsize = fontsize)
        if "y_ticks" in kwargs:
            ax.set_xticks(kwargs["y_ticks"],fontsize = fontsize)
        
        if legend:
            ax.legend(loc = 'best',prop= font )
        if "title" in kwargs:
            ax.set_title(kwargs["title"],fontproperties = font)

        plt.tight_layout()
        return ax
        

    def save(self, path, **kwargs):
        self.fig.savefig(path,**kwargs)


    def show(self):
        plt.show()