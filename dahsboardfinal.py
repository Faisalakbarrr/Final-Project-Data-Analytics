# -*- coding: utf-8 -*-
"""DahsboardFinalBikeSharing

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1t-P8K-UCtfZBZqpfLQzRWzPDvuT4A3sl
"""

!pip install streamlit


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data
from google.colab import files
uploaded = files.upload()

# Load data from csv files
allbikesharing = pd.read_csv("hour.csv")

def plot_season_rentals():
    # Menghitung jumlah peminjam sepeda per musim
    season_rentals = allbikesharing.groupby('season').mean()['cnt']

    # Membuat plot
    plt.figure(figsize=(8, 6))
    plt.bar(season_rentals.index, season_rentals.values)
    plt.xlabel('Musim')
    plt.ylabel('Total Transaksi')
    plt.title('Total Transaksi per musim')
    st.pyplot()

def plot_weather_count():
    # Mengetahui pengaruh cuaca terhadap jumlah transaksi
    weather_count = allbikesharing.groupby('weathersit')['cnt'].sum()
    weather_count.plot(kind='bar')
    plt.title('Total Transaksi per Cuaca')
    plt.xlabel('Cuaca')
    plt.ylabel('Total Transaksi')
    plt.xticks(rotation=0)
    st.pyplot()

def plot_holiday_count():
    # Apakah hari libur atau hari kerja mempengaruhi jumlah peminjam sepeda
    holiday_count = allbikesharing.groupby('holiday')['cnt'].sum()
    holiday_count.plot(kind='bar')
    plt.title('Total Transaksi pada Hari Libur dan hari kerja')
    plt.xlabel('Hari Libur')
    plt.xlabel('hari kerja (0 = hari kerja, 1 = Holiday / Weekend)')
    plt.ylabel('Total Transaksi')
    plt.xticks(rotation=0)
    st.pyplot()

def plot_hour_count():
    # Mengetahui pengaruh waktu (jam) terhadap jumlah transaksi
    hour_count = allbikesharing.groupby('hr')['cnt'].sum()
    hour_count.plot(kind='line')
    plt.title('Total Transaksi pada Setiap Jam')
    plt.xlabel('Jam')
    plt.ylabel('Total Transaksi')
    plt.xticks(np.arange(0, 24, step=1))
    st.pyplot()

# Define app layout
st.set_page_config(page_title="Bike Sharing Demand Dashboard", layout="wide")

st.title("Bike Sharing Demand Dashboard")

# Add a sidebar
st.sidebar.title("Navigation")
menu = ["Home", "Musim", "Cuaca", "Hari", "Jam"]
choice = st.sidebar.radio("Pilih menu", menu)

# Display the selected menu
if choice == "Home":
    st.header("Selamat datang di Bike Sharing Demand Dashboard!")
    st.write("Silakan pilih menu di sidebar untuk melihat visualisasi data.")
elif choice == "Musim":
    st.header("Total Transaksi per musim")
    plot_season_rentals()
elif choice == "Cuaca":
    st.header("Total Transaksi per Cuaca")
    plot_weather_count()
elif choice == "Hari":
    st.header("Total Transaksi pada Hari Libur dan hari kerja")
    plot_holiday_count()
else:
    st.header("Total Transaksi pada Setiap Jam")
    plot_hour_count()