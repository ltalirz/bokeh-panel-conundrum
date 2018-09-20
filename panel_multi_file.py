# panels.py
from bokeh.models.widgets import Tabs
from bokeh.io import output_file, show, curdoc
from bokeh.layouts import layout
from bokeh.plotting import figure

output_file("slider.html")

from panel1 import tab1

tabs = Tabs(tabs=[ tab1 ])

l = layout(tabs)
curdoc().add_root(l)
