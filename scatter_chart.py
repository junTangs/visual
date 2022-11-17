from .base_chart import BaseChart,mpl,plt

class ScatterChart(BaseChart):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def draw_ax(self, data, ax,with_line = True,legend = True, **kwargs):
        for value in data["values"]:
            if "marker" not in value["option"]:
                value["option"]["marker"] = 'o'
            if with_line:
                ax.plot(value["x"],value["y"],**value["option"])
            else:
                ax.scatter(value["x"],value["y"],**value["option"])
        return super().draw_ax(data,ax,legend,**kwargs)  

    def draw(self, data,figsize = (5,5), legend= True,**kwargs):
        with plt.style.context(['visual/style/ieee-line.mplstyle','visual/style/grid.mplstyle']):
            self.fig, ax = plt.subplots(ncols=1,nrows=1,figsize = figsize)

            self.draw_ax(data,ax,legend, **kwargs)
            
            if self._draw_callback is not None:
                self._draw_callback(self.fig,ax,data)
            return 
    
    def save(self, path, **kwargs):
        self.fig.savefig(path)

    def show(self):
        plt.show()


if __name__ == "__main__":
    data  = {
            "values":[
                {"x":list(range(10)),"y":list(range(10)),"option":{"linewidth":2,"label":"test","marker" :'*'}},
                {"x":list(range(10)),"y":list(range(10)),"option":{"linewidth":2,"label":"test2","marker":"^"}}
                ]}

    sc = ScatterChart()
    sc.draw(data,legend  = True)
    sc.save("sc_test.png")
