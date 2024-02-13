import pandas as pd
import numpy as np
import streamlit as st

st.title ("Singapore Map")
df = pd.DataFrame(np.random.randn(500, 2) / [50, 50] + [1.35, 103.8],columns=['lat', 'lon'])
st.map(df)