from .base_chart import BaseChart,mpl,plt
import numpy as np
import pandas as pd 

class BarChart(BaseChart):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        
    
    def draw_ax(self, data, ax,legend = True,**kwargs):
        d = {}

        for value in data["values"]:
            d[value["option"]["label"]] = value['y']
        df = pd.DataFrame(data=d,index=data["x"])
        if kwargs.get("barh",False):
            ax = df.plot.barh(ax = ax,rot = 0)
        else:
            ax = df.plot.bar(ax = ax,rot = 0)

        if kwargs.get("anno",False):
            for bar_group in ax.containers:
                ax.bar_label(bar_group,padding=1,fontsize = kwargs.get("fontsize",10))
        return super().draw_ax(data, ax,legend,**kwargs)

    def draw(self, data,figsize = (7,7),legend = True, **kwargs):
        super().draw(data,['visual/style/ieee-bar.mplstyle'],figsize,legend,**kwargs)
        return 



            
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