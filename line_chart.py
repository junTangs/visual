from .base_chart import BaseChart,plt
from .basic_draw import add_anno

class LineChart(BaseChart):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)


    def draw_ax(self,data,ax,legend = True,**kwargs):
    
        for value in data["values"]:
            ax.plot(data["x"],value["y"],**value["option"])
            if kwargs.get("anno",False):
                for x,y in zip(data["x"],value["y"]):
                    add_anno(ax=ax,x=x,y=y,x_txt=x,y_txt=y,text=f"{y}",fontsize = kwargs.get("fontsize",15))

        
        return super().draw_ax(data,ax,legend,**kwargs)  
    
    def draw(self, data,figsize = (7,7),legend = True, **kwargs):
        super().draw(data,['visual/style/ieee-line.mplstyle',"visual/style/no-latex.mplstyle","visual/style/grid.mplstyle"],figsize,legend,**kwargs)
        return 

            
if __name__ == "__main__":
    import math

    data  = {"x":list(range(10)),
            "values":[
                {"y":list(range(10)),"option":{"linewidth":2,"label":"test"}},
                {"y":list(range(10)),"option":{"linewidth":2,"label":"test2"}}
                ]}

    lc = LineChart()
    lc.draw(data,legend  = True)
    lc.save("test.png")

        
        
                
                
            
            
