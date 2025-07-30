import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

#NOMBRE DE LA PESTAÑA
st.set_page_config(layout='centered',
                   page_title='Talento tech',
                   page_icon=':smile:')

#TITULO DE LA PAGINA

t1,t2 =st.columns([0.3,0.7])
t1.image('bonita-imagen.jpg', width = 420)
t2.title('Tablero')
t2.markdown('**tel:** 123 | email: diego.lopez@streamlit.com',)

#SECCIONES
steps = st.tabs(['Pestaña', 'Pestaña 2', 'Pestaña $\sqrt{9}$'])
with steps[0]:
    camp_df = pd.read_csv('Campanhas.csv', encoding='latin1', sep=';')
    camp = st.selectbox('Escoge un ID de campaña', camp_df['ID_Campana'], help= 'Muestra las campañas existentes')
    
    metdf = pd.read_csv('Metricas.csv', encoding='latin1', sep=';')
    st.dataframe(metdf)
    m1,m2,m3 = st.columns([1,1,1])
    id1 = metdf[(metdf['ID_Campana']== camp)]
    id2 = metdf[(metdf['ID_Campana']== camp)]
    m1.write('Métricas filtradas')

    m1.metric(label= 'Métrica 1', value= sum(id1['Conversiones']),
              delta=str(sum(id1['Rebotes']))+'Número de rebotes', delta_color='inverse')
    m2.metric(label= 'Metrica 2', value= np.mean(id1['Clics']),delta=str(np.mean(id1['Impresiones']))+'Número de rebotes', delta_color='inverse')

    st.pyplot(fig)

    
