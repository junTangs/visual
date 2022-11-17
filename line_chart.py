from .base_chart import BaseChart,plt


class LineChart(BaseChart):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)


    def draw_ax(self,data,ax,legend,**kwargs):
    
        for value in data["values"]:
            ax.plot(data["x"],value["y"],**value["option"])

        return super().draw_ax(data,ax,legend,**kwargs)  



    def draw(self, data,figsize = (5,5), legend = True,**kwargs):
        with plt.style.context(['visual/style/ieee-line.mplstyle',"visual/style/no-latex.mplstyle"]):
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

    lc = LineChart()
    lc.draw(data,legend  = True)
    lc.save("test.png")

        
        
                
                
            
            
