# import bokeh.io
# import bokeh.plotting
# from bokeh.plotting import figure,output_file,show
# from  bokeh.sampledata.iris import flowers
# bokeh.io.output_notebook()

# p=bokeh.plotting.figure()
# bokeh.io.output_notebook()

# import bokeh.io
# import bokeh.plotting
# from bokeh.plotting import figure,output_file,show
# from  bokeh.sampledata.iris import flowers
# # output_file("iris.html")
# p=figure(title="Iris Morphology")

# p.xaxis.axis_label="Petal Length"
# p.yaxis.axis_label="Petal Width"
# p.circle(flowers["petal_length"],flowers["petal_width"])
# show(p)


import bokeh.io
import bokeh.plotting
from bokeh.plotting import figure,output_file,show
from  bokeh.sampledata.iris import flowers
# output_file("iris.html")
p=figure(title="Iris Morphology")

p.xaxis.axis_label="Petal Length"
p.yaxis.axis_label="Petal Width"
p.circle(flowers["petal_length"],flowers["petal_width"])
show(p)

x=[1,2,3,4,5]
y=[3,4,5,6,7]
output_file("line.html")
p=figure(title="line plot")
p.scatter(x,y,fill_color="red",legend_lable='red point',size=20)
show(p)

