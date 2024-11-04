import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data_points = pd.DataFrame(np.random.randn(20,3), columns = ["Col-1","Col-2","Col-3"])
st.table(data_points.head())
st.header("1. Charts with Random Numbers")
st.subheader("1.1 Line Chart")
st.line_chart(data_points)

st.subheader("1.2 Area Chart")
st.area_chart(data_points)

st.subheader("1.3 Bar Chart")
st.bar_chart(data_points)

st.header("2. Plotting graphs with Matplotlib and Seaborn")
st.subheader("2.1 Loading the CSV File")
iris_data = pd.read_csv(r"C:\Users\ssvak\PYTHON 2024\python2024\Streamlit\iris.csv")
st.table(iris_data)

st.subheader("2.2 Plotting Species bar data with matplotlib")
fig = plt.figure(figsize = (18,5))
iris_data['species'].value_counts().plot(kind = "bar")
st.pyplot(fig)

st.subheader("2.3 Plotting Distribution Data with Seaborn")
fig = plt.figure(figsize = (18,5))
sns.distplot(iris_data['sepal_length'])
st.pyplot(fig)

st.header("3.Multiple columns in a graph")
col1, col2 = st.columns(2)
with col1:
    col1.header("KDE = False")
    fig1 = plt.figure(figsize = (18,5))
    sns.distplot(iris_data['sepal_length'], kde = False)
    st.pyplot(fig1)

with col2:
    col2.header("Hist = False")
    fig2 = plt.figure(figsize = (18,5))
    sns.distplot(iris_data['sepal_length'], hist = False)
    st.pyplot(fig2)

st.subheader("4. Changing the Styles")
col1, col2 = st.columns(2)
with col1:
    col1.header("KDE = False")
    fig1 = plt.figure()
    sns.set_style('darkgrid')
    sns.set_context('notebook')
    sns.distplot(iris_data['petal_length'], kde = False)
    st.pyplot(fig1)
with col2:
    col2.header("Hist = False")
    fig2 =plt.figure()
    sns.set_theme(context = "poster", style = "darkgrid")
    sns.distplot(iris_data['petal_length'], hist = False)
    st.pyplot(fig2)

st.header("5.Exploring Multiple Graph types")
st.subheader("5.1 Scatter Plot")
fig, ax = plt.subplots(figsize=(18,5))
ax.scatter(*np.random.random(size=(2,100)))
st.pyplot(fig)

st.subheader("5.2 Count Plot")
fig = plt.figure(figsize = (18,5))
sns.countplot(data = iris_data, x = "species")
st.pyplot(fig)

st.subheader("5.3 Violin Plot")
fig = plt.figure(figsize = (18,5))
sns.violinplot(data = iris_data, x = "species", y = "sepal_length")
st.pyplot(fig)

st.subheader("5.4 Box Plot")
fig = plt.figure(figsize = (18,5))
sns.boxplot(data = iris_data, x = "species", y = "sepal_length")
st.pyplot(fig)