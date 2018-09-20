from bokeh.models.widgets import Panel, Tabs
from bokeh.io import output_file, show, curdoc
from bokeh.layouts import layout
from bokeh.plotting import figure

output_file("slider.html")

p1 = figure(plot_width=300, plot_height=300)
p1.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5)
tab1 = Panel(child=p1, title="line")

tabs = Tabs(tabs=[ tab1 ])

l = layout(tabs)
curdoc().add_root(l)
