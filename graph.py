import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import altair as alt
import graphviz as graphviz

# Graph Chart
st.graphviz_chart('''    digraph {        Big_shark -> Tuna        Tuna -> Mackerel        Mackerel -> Small_fishes        Small_fishes -> Shrimp    }''')

# Alternate
df=pd.DataFrame(np.random.randn(500, 3), columns=['x','y','z'])
c=alt.Chart(df).mark_circle().encode(x="x", y="y" , size='z', color='z', tooltip=['x', 'y', 'z'])
st.altair_chart(c, use_container_width=True)

# area charts

df= pd.DataFrame(    np.random.randn(10, 2),    columns=['x', 'y'])
st.area_chart(df)

# Bar charts
df= pd.DataFrame(    np.random.randn(10, 2),    columns=['x', 'y'])
st.bar_chart(df)

# Histogram
rand=np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)


# Line charts
df= pd.DataFrame(    np.random.randn(10, 2),    columns=['x', 'y'])
st.line_chart(df)