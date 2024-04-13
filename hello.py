import pandas as pd
import streamlit as st
import plotly.express as px

data = pd.read_csv('iris_data.csv')

st.set_page_config(
		page_title='Iris Dataset',
		# layout='wide'
	)
st.title('Visualisasi Sederhana dengan Iris')
st.write("")
col1, col2 = st.columns([2,6])

with st.sidebar:
	st.markdown("**Pilih Spesies**")
	setosa_on = st.checkbox('Iris Setosa')
	versicolor_on = st.checkbox('Iris Versicolor')
	virginica_on = st.checkbox('Iris Virginica')

toggle_list = []
if setosa_on:
	toggle_list.append('Iris-setosa')
if versicolor_on:
	toggle_list.append('Iris-versicolor')
if virginica_on:
	toggle_list.append('Iris-virginica')

data_filter_species = data.query('Species in @toggle_list')

if toggle_list:
	used_data = data_filter_species
else:
	used_data = data

# with col2:
st.dataframe(used_data, use_container_width=True)

col3, col4 = st.columns(2)

with col3:
	st.markdown("**Distribusi Petal Length**")
	fig1 = px.histogram(used_data, x = 'PetalLengthCm', color='Species')
	st.plotly_chart(fig1, use_container_width=True)

with col4:
	st.markdown("**Distribusi Sepal Length**")
	fig1 = px.histogram(used_data, x = 'SepalLengthCm', color='Species')
	st.plotly_chart(fig1, use_container_width=True)

st.markdown("**Korelasi Antar Variabel**")
var1 = st.radio(
		"Pilih Variabel X",
		data.columns.tolist()[:-1],
		horizontal = True
	)
var2 = st.radio(
		"Pilih Variabel Y",
		data.columns.tolist()[:-1],
		horizontal = True
	)

fig5 = px.scatter(
	used_data, x = var1, y = var2,
	hover_data = [var1, var2],
	color = 'Species')

st.plotly_chart(fig5, use_container_width=True)