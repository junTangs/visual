from .base_chart import BaseChart,mpl,plt
import numpy as np
import pandas as pd 

class BarChart(BaseChart):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        
    
    def draw_ax(self, data, ax,bar_width = 0.1, legend = True,**kwargs):
        d = {}
        for value in data["values"]:
            d[value["option"]["label"]] = value['y']
        df = pd.DataFrame(data=d,index=data["x"])
        ax = df.plot.bar(ax = ax,rot = 0)
        return super().draw_ax(data, ax,legend,**kwargs)

    def draw(self, data,figsize = (5,5),legend = True, **kwargs):
        with plt.style.context(['visual/style/ieee-bar.mplstyle']):
            self.fig, ax = plt.subplots(ncols=1,nrows=1,figsize = figsize)
            
            self.draw_ax(data,ax,legend,**kwargs)
            
            if self._draw_callback is not None:
                self._draw_callback(self.fig,ax,data)
            

            return 

    
    def save(self, path, **kwargs):
        self.fig.savefig(path)

    def show(self):
        plt.show()


            
if __name__ == "__main__":
    import math

    data  = {"x":list(range(10)),
            "values":[
                {"y":list(range(10)),"option":{"linewidth":2,"label":"test"}},
                {"y":list(range(10)),"option":{"linewidth":2,"label":"test2"}}
                ]}

    bc = BarChart()
    bc.draw(data)
    bc.save("bc_test.png")