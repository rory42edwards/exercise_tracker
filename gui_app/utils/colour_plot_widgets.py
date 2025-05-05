from pyqtgraph import PlotWidget, mkPen


def set_plot_widget_dark(graphWidget: PlotWidget):
    plot = graphWidget.getPlotItem()

    # Set background
    graphWidget.setBackground('#121212')

    # Set axis text colour
    plot.getAxis('bottom').setTextPen('#E0E0E0')
    plot.getAxis('left').setTextPen('#E0E0E0')


def set_plot_widget_light(graphWidget: PlotWidget):
    plot = graphWidget.getPlotItem()

    # Set background
    graphWidget.setBackground('#FAFAFA')

    # Set axis text colour
    plot.getAxis('bottom').setTextPen('#212121')
    plot.getAxis('left').setTextPen('#212121')
