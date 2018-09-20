# panel1.py
from bokeh.plotting import figure
from bokeh.models.widgets import Panel

p1 = figure(plot_width=300, plot_height=300)
p1.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5)

tab1 = Panel(child=p1, title="line")
