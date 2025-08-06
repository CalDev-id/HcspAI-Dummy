import streamlit as st
import pandas as pd
import numpy as np

def dashboard_page():
    st.write("Ini halaman Dashboard dengan grafik atau ringkasan data.")
    data = pd.DataFrame({
        "Hari": pd.date_range(start="2025-08-01", periods=10),
        "Nilai": np.random.randint(50, 100, 10)
    })
    st.line_chart(data.set_index("Hari"))
