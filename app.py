import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px 
from PIL import Image

st.set_page_config(page_title="Healthy Diet", layout="wide")

dc = pd.read_csv('data_capstone_clean.csv')
da = dc
da['rank'] = da.groupby('year')['percentage'].rank(method='max')
dc_gdp20lebih = dc.loc[(dc['gdp_per_capita'] >= 20000) & (dc['year'] == 2017)]
dc_gdp20kurang = dc.loc[(dc['gdp_per_capita'] < 20000) & (dc['year'] == 2017)]
data_2017 = dc[dc['year'] == 2017]
data_2018 = dc[dc['year'] == 2018]
data_2019 = dc[dc['year'] == 2019]
data_2020 = dc[dc['year'] == 2020]
indonesia = dc[dc['country'].str.contains('Indonesia')]
sea = dc[dc['country'].str.contains('Indonesia|Malaysia|Singapore|Thailand|Philippines|Vietnam|Myanmar|Cambodia')]
#dc_top = dc.sort_values(by=['percentage','years'], ascending=True).head(10)
#dc_top17 = dc[dc['year'] == 2017].sort_values(by='percentage', ascending=True).head(10)

st.title("Apakah Healthy Diet Mahal?")

st.header("Healthy Diet")

col1, col2 = st.columns([3,2])
with col1:
    st.markdown('<div style="text-align: justify;">Healthy Diet adalah Mengkonsumsi pola makan yang sehat di sepanjang siklus hidup membantu mencegah malnutrisi dalam segala bentuknya serta berbagai penyakit tidak menular (PTM) dan kondisi. Namun, peningkatan produksi makanan olahan, urbanisasi yang cepat, dan perubahan gaya hidup telah menyebabkan pergeseran pola makan. Orang-orang sekarang mengonsumsi lebih banyak makanan tinggi energi, lemak, gula bebas dan garam/natrium, dan banyak orang tidak makan cukup buah, sayuran dan serat makanan lainnya seperti biji-bijian utuh. Susunan yang tepat dari pola makan yang beragam, seimbang dan sehat akan bervariasi tergantung pada karakteristik individu (misalnya usia, jenis kelamin, gaya hidup, dan tingkat aktivitas fisik), konteks budaya, makanan yang tersedia secara lokal, dan kebiasaan makan. Namun, prinsip-prinsip dasar dari apa yang merupakan pola makan sehat tetap sama. </div>', unsafe_allow_html=True)
    #st.write('(Sumber : who.int/news-room/fact-sheets/detail/healthy-diet)')
    st.text(" ")
    st.markdown("##### Tabel data yang digunakan")
    st.dataframe(dc)
    st.write("(Sumber data:   World bank & OurWorldinData)")

with col2:
    st.text(" ")
    # st.markdown("### Tabel Korelasi")
    # fig1, ax = plt.subplots()
    # sns.heatmap(dc.corr(method='pearson'), cmap='Blues', annot=True, ax=ax)
    # st.write(fig1)
    st.text(" ")
    
st.markdown("---")


#world Chart

st.header('World ')

# col1, col2 = st.columns([2,4])
# with col1:
    #tahun_pilihan = dc['year'].unique().tolist()
    #tahun = st.selectbox('Pilih Tahun', tahun_pilihan)
    #dt = dc[dc['year']==tahun]
# with col2:
    #fig  = px.scatter(dt, x='Yearly_cost_healthy_diet', y='households_expenditure_per_capita', color='country', hover_name='country', log_x=True, size_max=100,title='pengeluaran Healthy Diet dari Total Pengeluaran',
                #labels={
                     #"Yearly_cost_healthy_diet": "pengeluaran Healthy Diet",
                     #"households_expenditure_per_capita": "Total Pengeluaran"
                 #},)
    #st.write(fig)

tahun_pilihan = dc['year'].unique().tolist()
temp_options = ['2017','2018','2019','2020']
temp = st.select_slider('Pilih tahun', options=tahun_pilihan)
st.write("Tahun yang dipilih:",temp)

dt = dc[dc['year'] == temp].sort_values(by='percentage', ascending=True).head(5)
dl = dc[dc['year'] == temp].sort_values(by='percentage', ascending=False).head(5)

col1, col2 = st.columns([2,2])
with col1:
    fig = px.bar(dt, x='percentage' , y='country', color='country', title='Top 5 countries cheap healthy diet', text_auto='.3f')
    fig.update_xaxes(range=[0,10])
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    #fig.update_layout(yaxis=dict(autorange="reversed"))
    st.write(fig)

with col2:
    fig = px.bar(dl, x='percentage' , y='country', color='country', title='Top 5 countries expensive healthy diet', text_auto='.3f')
    fig.update_xaxes(range=[0,550])
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    #fig.update_layout(yaxis=dict(autorange="reversed"))
    st.write(fig)

st.markdown("""
    DIlihat dari chart diatas selama tahun 2017-2020 luxembourg, Ireland, dan Switzerland menjadi 3 negara teratas dengan pengeluaran healthy diet termurah.
    Sedangkan Burundi, Central Africa Republic, dan Mozambique menjadi 3 negara teratas dengan pengeluaran healthy diet termahal.
    Luxembourg menjadi peringkat 1 pengeluaran healthy diet termurah dan memiliki kategori Very Cheap dengan nilai 0.8 secara terus menerus selama tahun 2017-2020. 
    Selanjutnya terdapat Ireland yang berada pada peringkat 2 memiliki nilai 0.9 pada tahun 2020, nilai ini turun 0.1 dari pada tahun-tahun sebelumnya yang bernilai 1.
    Pada negara dengan pengeluaran healthy diet termahal, Burundi menjadi peringkat 1 dengan nilai 429.4 pada tahun 2017 dan pada tahun 2020 nilai burundi naik menjadi 453.1 yang membuat negara burundi pengeluaran healthy dietnya semakin mahal.
    """)
st.write(" ")
st.write(" ")

col1, col2 = st.columns([3,2])

with col1:
    tab1, tab2, tab3, tab4 = st.tabs(['Rank World','GDP per capita < $20000','GDP per capita >= $20000','Trend Line'])
    with tab1:      
        fig = px.line(da, x='year', y='rank', color='country')
        fig.update_layout(yaxis=dict(range=[0,150]))
        fig.update_traces(mode="markers+lines")
        fig.update_xaxes(showgrid=False)
        st.write(fig)
    with tab2:
        fig = px.pie(dc_gdp20kurang, values=dc_gdp20kurang['category'].value_counts().values, names=dc_gdp20kurang['category'].value_counts().index, labels={'names':'Category','values':'Count'})
        fig.update_traces(textfont_size=20)
        fig.update_layout(margin=dict(t=50, b=50, l=50, r=200))
        st.write(fig)
    with tab3:
        fig = px.pie(dc_gdp20lebih, values=dc_gdp20lebih['category'].value_counts().values, names=dc_gdp20lebih['category'].value_counts().index, labels={'names':'Category','values':'Count'})
        fig.update_traces(textfont_size=20)
        fig.update_layout(margin=dict(t=50, b=50, l=50, r=200))
        st.write(fig)
    with tab4:
        fig2 = sns.lmplot(data=dc, x='gdp_per_capita', y='Yearly_cost_healthy_diet', hue='year')
        plt.title('Pengeluaran Healthy Diet terhadap Total Pendapatan')
        st.pyplot(fig2)

with col2:
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.markdown("""Pada bagain rank world disamping terlihat secara sekilas terdapat 2 negara yang peringkatnya mengalami penurunan secara signifikan yaitu sudan dan sint maarten.
        Pada tahun 2017 sudan berada pada peringkat 102 dan sint maarten pada peringkat 36. Ditahun-tahun selanjutnya peringkat kedua negara tersebut terus turun dan pada tahun 2020 sudan berada pada peringkat 141 dan sint maarten pada peringkat 88. 
        """)
        st.markdown("""Terdapat trend bahwa Semakin besar total pendapatan, Maka nilai dari pengeluaran Healthy Diet semakin kecil atau murah.
        """)
        st.markdown("""Lebih dari 70% negara memiliki total pendapatan dibawah $20.000, Dalam 70% negara terebut terdapat 50% negara yang pengeluaran Healthy Dietnya tergolong MAHAL dan 50% negara memiliki pengeluaran Healthy Diet yang tergolong MURAH.
        """)
        st.markdown("""Kurang dari 30% negara memiliki total pendapatan diatas $20.000, memiliki pengeluaran Healthy Diet yang tergolong MURAH.
        """)



st.markdown("---")


#indonesia chart 

st.header('Indonesia')
col1, col2= st.columns([2,3])
with col1:
    #st.dataframe(indonesia)
    st.write("")
    st.write("")
    st.write("")
    st.markdown("""
    Indonesia berada pada peringkat 101 pada tahun 2017 dan pada tahun tahun selanjutnya peringkat indonesia mengalami kenaikan hingga pada tahun 2020 indonesia berada pada peringkat 98 dari total 146 negara. Selain itu indonesia berada pada peringkat 4 dari total 8 negara yang berada di wilayah asia tenggara yang tercatat.\n
    Indonesia menjadi salah satu negara yang berkategori Expensive selama tahun 2017 - 2020 dengan nilai 41.5 pada tahun 2020. Pada tahun 2019 indonesia sempat berada pada nilai 37.1 yang nilai tersebut 2 lebih rendah dari pada tahun 2018 yang bernilai 39.5 dan 4 lebih rendah dari pada tahun 2020 yang bernilai 41.5.\n
    Indonesia sendiri memiliki pengeluaran healthy diet berkisar pada harga \$4.2 per hari dan pengeluaran rata-rata setiap tahunnya menghabiskan sebanyak \$1500.\n
    Di indonesia pengeluaran Healthy Diet tiap tahun mengalami kenaikan sekitar 3%. Adapun persentase pengeluaran Healthy Diet terhadap Total Pendapatan per kapita di Indonesia mencapai rata-rata 39.5%, dan mengalami kenaikan rata-rata sekitar 1.5% per tahun.\n
    Dengan nilai persentase rata-rata berada di angka 39.5% ini membuat negara indonesia memiliki kategori Expensive.
    """)

with col2:
    tab1,tab2,tab3 = st.tabs(['Rank Indonesia','Bar Plot','Line Plot'])
    with tab1:
        fig = px.line(sea, x='year', y='rank', color='country')
        fig.update_layout(yaxis=dict(range=[0,150]))
        fig.update_traces(mode="markers+lines")
        fig.update_xaxes(showgrid=False)
        st.write(fig)
    with tab2:
        fig = px.bar(indonesia, x='year' , y='percentage', text_auto=True)
        fig.update_yaxes(range=[0,100])
        st.write(fig)
    with tab3:
        fig = px.line(indonesia, x='year', y=['gdp_per_capita','households_expenditure_per_capita','Yearly_cost_healthy_diet'], labels={'y':'Value ($)'} )
        fig.update_layout(yaxis=dict(range=[0,4500]))
        fig.update_traces(mode="markers+lines")
        fig.update_xaxes(showgrid=False)
        st.write(fig)



#col1, col2, col3= st.columns(3)
#col1.metric("Total Pengeluaran terhadap total Pendapatan", "58%", "2%")
#col2.metric("Pengeluaran Healthy Diet terhadap Total Pendapatan", "39.5%", "1.5%")
#col3.metric("Pengeluaran Healthy Diet terhadap Total Pengeluaran", "68.5%", "5%")


st.markdown("---")


#Number of Countries by Category

st.markdown('## Number of Countries by Category')

tab1, tab2, tab3, tab4 = st.tabs(["2017", "2018", "2019", "2020"])
with tab1:
    col1, col2 = st.columns([4,3])
    with col1:
        fig = px.pie(data_2017, values=data_2017['category'].value_counts().values, names=data_2017['category'].value_counts().index, labels={'names':'Category','values':'Count'})
        fig.update_traces(textfont_size=20)
        fig.update_layout(margin=dict(t=50, b=50, l=50, r=50))
        st.write(fig)

    with col2:
        st.header(" ")
        st.header(" ")
        st.markdown("""
        Pada tahun 2017 dapat dilihat pada pie chart terdapat 146 negara dan sebanyak 36.3% atau 53 negara berada pada kategori Very Cheap dan 26% atau 38 negara berada pada kategori Very Expensive. 
        Negara yang memiliki kategori Healthy Diet mahal yaitu negara yang berada pada kategori expensive dan very expensive yang jumlahnya mencapai 54 negara(37%). 
        dan negera yang memiliki Healthy Diet murah yaitu negara yang berada pada kategori Very Cheap, Cheap, dan Medium yang jumlahnya mencapai 92 negara(63%).
        Sehingga dapat disimpulkan mayoritas negara memiliki kategori Healthy Diet yang tergolong MURAH.
        """)

with tab2:
    col1, col2 = st.columns([4,3])
    with col1:
        fig = px.pie(data_2018, values=data_2018['category'].value_counts().values, names=data_2018['category'].value_counts().index, labels={'names':'Category','values':'Count'})
        fig.update_traces(textfont_size=20)
        fig.update_layout(margin=dict(t=50, b=50, l=50, r=50))
        st.write(fig)

    with col2:
        st.header(" ")
        st.header(" ")
        st.markdown("""
        Pada tahun 2018 dapat dilihat pada pie chart terdapat 144 negara dan sebanyak 38.2% atau 55 negara berada pada kategori Very Cheap dan 27.1% atau 39 negara berada pada kategori Very Expensive. 
        Negara yang memiliki kategori Healthy Diet mahal yaitu negara yang berada pada kategori expensive dan very expensive yang jumlahnya mencapai 51 negara(35.4%) 
        dan negera yang memiliki Healthy Diet murah yaitu negara yang berada pada kategori Very Cheap, Cheap, dan Medium yang jumlahnya mencapai 93 negara(64.6%).
        Sehingga dapat disimpulkan mayoritas negara memiliki kategori Healthy Diet yang tergolong MURAH.
        """)

with tab3:
    col1, col2 = st.columns([4,3])
    with col1:
        fig = px.pie(data_2019, values=data_2019['category'].value_counts().values, names=data_2019['category'].value_counts().index, labels={'names':'Category','values':'Count'})
        fig.update_traces(textfont_size=20)
        fig.update_layout(margin=dict(t=50, b=50, l=50, r=50))
        st.write(fig)
    
    with col2:
        st.header(" ")
        st.header(" ")
        st.markdown("""
        Pada tahun 2019 dapat dilihat pada pie chart terdapat 144 negara dan sebanyak 36.8% atau 53 negara berada pada kategori Very Cheap dan 26.4% atau 38 negara berada pada kategori Very Expensive. 
        Negara yang memiliki kategori Healthy Diet mahal yaitu negara yang berada pada kategori expensive dan very expensive yang jumlahnya mencapai 52 negara(36.1%) 
        dan negera yang memiliki Healthy Diet murah yaitu negara yang berada pada kategori Very Cheap, Cheap, dan Medium yang jumlahnya mencapai 92 negara(63.9%).
        Sehingga dapat disimpulkan mayoritas negara memiliki kategori Healthy Diet yang tergolong MURAH.
        """)

with tab4:
    col1, col2 = st.columns([4,3])
    with col1:
        fig = px.pie(data_2020, values=data_2020['category'].value_counts().values, names=data_2020['category'].value_counts().index, labels={'names':'Category','values':'Count'})
        fig.update_traces(textfont_size=20)
        fig.update_layout(margin=dict(t=50, b=50, l=50, r=50))
        st.write(fig)

    with col2:
        st.header(" ")
        st.header(" ")
        st.markdown("""
        Pada tahun 2020 dapat dilihat pada pie chart terdapat 144 negara dan sebanyak 33.3% atau 48 negara berada pada kategori Very Cheap dan 27.8% atau 40 negara berada pada kategori Very Expensive. 
        Negara yang memiliki kategori Healthy Diet mahal yaitu negara yang berada pada kategori expensive dan very expensive yang jumlahnya mencapai 55 negara(38.2%) 
        dan negera yang memiliki Healthy Diet murah yaitu negara yang berada pada kategori Very Cheap, Cheap, dan Medium yang jumlahnya mencapai 89 negara(61.8%).
        Sehingga dapat disimpulkan mayoritas negara memiliki kategori Healthy Diet yang tergolong MURAH.
        """)



st.markdown("---")

col1, col2 = st.columns(2)
    
x_axis_val = col1.selectbox('Pilih indikator 1(X-axis)', options=dc.columns)
y_axis_val = col2.selectbox('Pilih indikator 2(Y-axis)', options=dc.columns)

plot = px.scatter(dc, x=x_axis_val, y=y_axis_val, color='country', hover_name='year', log_x=True, size_max=100)
st.plotly_chart(plot, use_container_width=True)

