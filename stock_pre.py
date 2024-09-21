#import joblib
import streamlit as st
import pandas as pd
import numpy as np

file = "Stock.pkl"
model = joblib.load(file)
model1 = joblib.load("Stock1.pkl")

st.title("Stock Prediction")

#input
o = st.number_input("Open ")
h = st.number_input("High ")
l = st.number_input("Low")
v = st.number_input("Volume")


dataframe = pd.DataFrame({
	'Open':[o],
	'High':[h],
	'Low':[l],
	'Volume':[v],
	'high - low':[h - l],
})

# Prediction

if st.button("Predict"):
	close = model.predict(dataframe)
	risk = model1.predict(dataframe)
	st.write(close)
	a = (risk>0.499).astype(int)
	l = ["Not Risky", "Risky"]
	st.write(l[int(a)])
