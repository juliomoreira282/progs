import streamlit as st
import psutil
import pandas as pd
import time
import datetime

st.set_page_config(
    page_title="Monitor de Sistema em Tempo Real",
    page_icon="🖥️",
    layout="wide"
)

st.title("Dashboard de Monitoramento de Sistema em Tempo Real")

col1, col2 = st.columns(2)

with col1:
    cpu_gauge_placeholder = st.empty()

with col2:
    mem_gauge_placeholder = st.empty()

chart_placeholder = st.empty()

history_len = 60

data = {
    'Tempo': [datetime.datetime.now() - datetime.timedelta(seconds=i) for i in range(history_len, 0, -1)],
    'Uso de CPU (%)': [0] * history_len,
    'Uso de Memória (%)' : [0] * history_len
}

history_df = pd.DataFrame(data).set_index('Tempo')

while True:
    cpu_percent = psutil.cpu_percent(interval=None)
    mem_info = psutil.virtual_memory()
    mem_percent = mem_info.percent

    with cpu_gauge_placeholder.container():
        st.metric(
            label="Uso de CPU",
            value=f"{cpu_percent:.2f} %"
        )
    
    with mem_gauge_placeholder.container():
        st.metric(
            label="Uso de Memória RAM",
            value=f"{mem_percent:.2f}",
            delta=f"{mem_info.available / (1024 ** 3):.2f} GB Livres",
            delta_color="off"
        )
    
    current_time = datetime.datetime.now()
    new_data = pd.DataFrame({
        'Uso de CPU (%)': [cpu_percent],
        'Uso de Memória (%)': [mem_percent]
    }, index=current_time)

    history_df = pd.concat([history_df.tail(history_len - 1), new_data])

    with chart_placeholder.container():
        st.subheader("Histórico de Uso (Últimos 60 segundos)")
        st.line_chart(history_df)
    
    time.sleep(1)