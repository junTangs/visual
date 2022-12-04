import matplotlib as mpl
import matplotlib.pyplot as plt


def add_point(ax,x,y,color='r',marker = 'o',alpha = 1,size = 1,**kwargs):
    ax.scatter(x,y,color = color,alpha = alpha,marker = marker,s = size,**kwargs)
    
def add_text(ax,x,y,text,color='r',size = 10,**kwargs):
    ax.text(x,y,text,color = color,size = size,**kwargs)

def add_circle(ax,x,y,r,color='r',alpha = 1,**kwargs):
    ax.add_patch(plt.Circle((x,y),r,color = color,alpha = alpha,**kwargs))

def add_line(ax,x,y,x2,y2,color='r',alpha = 1,**kwargs):
    ax.add_line(plt.Line2D((x,x2),(y,y2),color = color,alpha = alpha,**kwargs))

def add_anno(ax,x,y,text,x_txt,y_txt,**kwargs):
    ax.annotate(text = text,xy = (x,y),xytext = (x_txt,y_txt),**kwargs)