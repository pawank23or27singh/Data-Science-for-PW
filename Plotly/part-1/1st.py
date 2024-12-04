import plotly.graph_objects as go

# fig=go.Figure(go.Scatter(x=[1,2,3,4,5],y=[3,4,5,6,7],mode='markers'))
# fig.show()

# fig=go.Figure()
# fig.add_trace(go.Scatter(x=[1,2,3,4,5],y=[3,4,5,6,7],mode='marker'))
# fig.show()

# fig=go.Figure(go.Bar(x=[1,2,3,4,5],y=[3,4,5,6,7]))
# fig.show()
# x=[1,2,4,13,17,10,21,13,4,15,6,17,8,29,10,17,17,46,34]
# fig=go.Figure(data=[go.Histogram(x=x)])
# fig.show()

# import seaborn as sns
# tips=sns.load_dataset('tips')

# fig=go.Figure(data=[go.Histogram(x=tips['total_bill'])])
# fig.show()


import seaborn as sns
tips=sns.load_dataset('tips')

fig=go.Figure()
fig.go.Scatter(x=tips.total_bill,y=tips.tip,mode='markers')
fig.show()