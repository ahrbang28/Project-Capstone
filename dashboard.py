import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px 
from PIL import Image

st.set_page_config(page_title="Apakah Healthy Diet Mahal?", layout="wide")

dc = pd.read_csv('hasil_data_capstone.csv')

st.title("Apakah Healthy Diet Mahal?")

st.markdown("## Healthy Diet")

col1, col2 = st.columns([3,2])
with col1:
    st.markdown("*Healthy Diet* atau Mengkonsumsi pola makan yang sehat di sepanjang siklus hidup membantu mencegah malnutrisi dalam segala bentuknya serta berbagai penyakit tidak menular (PTM) dan kondisi. Namun, peningkatan produksi makanan olahan, urbanisasi yang cepat, dan perubahan gaya hidup telah menyebabkan pergeseran pola diet. Orang-orang sekarang mengonsumsi lebih banyak makanan tinggi energi, lemak, gula bebas dan garam/natrium, dan banyak orang tidak makan cukup buah, sayuran dan serat makanan lainnya seperti biji-bijian utuh. Susunan yang tepat dari pola makan yang beragam, seimbang dan sehat akan bervariasi tergantung pada karakteristik individu (misalnya usia, jenis kelamin, gaya hidup, dan tingkat aktivitas fisik), konteks budaya, makanan yang tersedia secara lokal, dan kebiasaan makan. Namun, prinsip-prinsip dasar dari apa yang merupakan pola makan sehat tetap sama.")
    st.markdown("##### Tabel data yang digunakan")
    st.dataframe(dc)
with col2:
    
    st.markdown("### Tabel Korelasi")
    fig1, ax = plt.subplots()
    sns.heatmap(dc.corr(method='pearson'), cmap='Blues', annot=True, ax=ax)
    st.write(fig1)
    
st.text("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

indonesia = dc[dc['country'].str.contains('Indonesia')]
df = pd.DataFrame(indonesia ,columns=["Yearly_cost_healthy_diet", "gdp_per_capita", "households_expenditure_per_capita", 'year']).set_index('year')
uji = px.line(indonesia, x='year', y=['households_expenditure_per_capita','Yearly_cost_healthy_diet'])

#world Chart
st.markdown('## World Chart')
col1, col2 = st.columns(2)
    
x_axis_val = col1.selectbox('Pilih indikator 1(X-axis)', options=dc.columns)
y_axis_val = col2.selectbox('Pilih indikator 2(Y-axis)', options=dc.columns)

plot = px.scatter(dc, x=x_axis_val, y=y_axis_val, color='country', hover_name='year', log_x=True, size_max=100)
st.plotly_chart(plot, use_container_width=True)

col1, col2 = st.columns([2,4])
with col1:
    tahun_pilihan = dc['year'].unique().tolist()
    tahun = st.selectbox('Pilih Tahun', tahun_pilihan)
    dt = dc[dc['year']==tahun]
with col2:
    fig  = px.scatter(dt, x='Yearly_cost_healthy_diet', y='households_expenditure_per_capita', color='country', hover_name='country', log_x=True, size_max=100,title='pengeluaran Healthy Diet dari Total Pengeluaran',
                labels={
                     "Yearly_cost_healthy_diet": "pengeluaran Healthy Diet",
                     "households_expenditure_per_capita": "Total Pengeluaran"
                 },)
    st.write(fig)
col1, col2, col3 = st.columns(3)
with col1:
    fig1 = sns.lmplot(data=dc, x='households_expenditure_per_capita', y='Yearly_cost_healthy_diet', hue='year')
    plt.title('Pengeluaran Healthy Diet vs Total Pengeluaran')
    st.pyplot(fig1)
with col2:
    fig2 = sns.lmplot(data=dc, x='gdp_per_capita', y='Yearly_cost_healthy_diet', hue='year')
    plt.title('Pengeluaran Healthy Diet vs Total Pendapatan')
    st.pyplot(fig2)
with col3:
    st.markdown("""Semakin besar total pendapatan atau total pengeluaran suatu negara maka pengeluaran Healthy Diet dianggap kecil karena hanya mencakup sekitar 10% dari total pengeluaran yang memiliki nilai lebih dari $15.000
    """)
    st.markdown("""Terdapat trend bahwa Semakin besar total pengeluaran atau total pendapatan, nilai dari pengeluaran Healthy Diet semakin kecil
    """)
    st.markdown("""Lebih dari 50% negara yang memiliki nilai total pengeluaran dibawah $10.000, nilai dari pengeluaran Healthy Diet negara tersebut terhitung cukup besar
    """)

st.text("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
#indonesia chart 
data_capstone1 = indonesia[['year','households_expenditure_per_capita']]
data_capstone2 = indonesia[['year','Yearly_cost_healthy_diet']]


col1, col2, col3= st.columns(3)
with col1:
    st.markdown("## Indonesia Chart")
    st.dataframe(indonesia)

with col2:
    colo1 = 'steelblue'
    colo2 = 'red'

    fig2,ax = plt.subplots()
    ax.plot(data_capstone1.year, data_capstone1.households_expenditure_per_capita, color=colo1)
    ax.set_xlabel('Tahun', fontsize=8)
    ax.set_ylabel('Total Pengeluaran', color=colo1 ,fontsize=8)
    ax2 = ax.twinx()
    ax2.plot(data_capstone2.year, data_capstone2.Yearly_cost_healthy_diet, color=colo2)
    ax2.set_ylabel('pengeluaran Healthy Diet', color=colo2, fontsize=8)
    plt.title("pengeluaran Healthy Diet vs Total Pengeluaran")
    st.write(fig2)
with col3:
    st.markdown("      ")

    


col1, col2, col3= st.columns(3)
col1.metric("Total Pengeluaran terhadap total Pendapatan", "58%", "2%")
col2.metric("Pengeluaran Healthy Diet terhadap Total Pendapatan", "39.5%", "1.5%")
col3.metric("Pengeluaran Healthy Diet terhadap Total Pengeluaran", "68.5%", "5%")
st.markdown("""
Di negara Indonesia pengeluaran Healthy Diet tiap tahun mengalami kenaikan sekitar 3%.\n
Adapun persentase pengeluaran Healthy Diet terhadap Total Pendapatan di Indonesia mencapai 39.5%, dan mengalami kenaikan rata-rata sekitar 1.5% per tahun.\n
Persentase pengeluaran Healthy Diet terhadap Total Pengeluaran di indonesia mencapai 68.5% yang mana dapat dianggap bahwa pengeluaran Healthy Diet terhitung mahal.\n
""")

st.text("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

