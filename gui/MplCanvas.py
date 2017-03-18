from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy

from PyQt5.QtWidgets import QSizePolicy


class MatPlotLibCanvas(FigureCanvas):
    
    def __init__(self, parent=None, dpi=100):
        
        self.fig = Figure(dpi=dpi,frameon=True)#,tight_layout=True)
        
        self.axes = self.fig.add_subplot(111)
        
        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,QSizePolicy.Expanding,QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)     

    def update_figure(self, data = None,title="Dummy"):
        self.axes.clear()  

        self.axes.grid(b=True, which='minor', color='0.85',linestyle=':')
        self.axes.grid(b=True, which='major', color='0.55',linestyle=':')
        #self.axes.grid(b=True, which='both', color='0.75',linestyle=':')
        self.axes.minorticks_on()
        
        if data:
            for event in data:
                unit = "("+event.unit+")" if event.unit else ""
                g, = self.axes.plot( event.labels,event.data,label=event.name+unit)
                g.set_drawstyle('steps-mid')
                
        self.axes.set_title(title,fontsize=30)
        self.axes.set_xlabel("XLabel")
        self.axes.set_ylabel("YLabel")
        self.axes.legend()
        self.draw()
        self.fig.tight_layout()