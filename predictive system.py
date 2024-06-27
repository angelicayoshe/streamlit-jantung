# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pickle
import pandas as pd

# Function to predict disease category based on restingBP range
def predict_disease_category(restingBP_range):
    # Define the rules for predicting disease category based on restingBP range
    if restingBP_range > 140:
        return 'Jantung Koroner'
    elif 110 <= restingBP_range < 120:
        return 'Endokarditis'
    elif 120 <= restingBP_range < 140:
        return 'Aritmia'
    elif 130 <= restingBP_range > 140:
        return 'Jantung Bawaan'
    elif restingBP_range >= 140:
        return 'Gagal Jantung'


# Gunakan path absolut ke file model
loaded_model = pickle.load(open('C:/Users/User/Downloads/Data Modelling/Deployment/trained_model.sav', 'rb'))

# Muat dataset dari file Excel
file_path = 'C:/Users/User/Downloads/Data Modelling/Deployment/hearrtss.xlsx'  # Ganti dengan path ke file dataset Anda
df = pd.read_excel(file_path)

# Pastikan kolom 'RestingBP' ada dalam dataset
if 'RestingBP' in df.columns:
    # Predict disease category based on restingBP range for each row
    predicted_categories = df['RestingBP'].apply(predict_disease_category)

    # Display the predicted disease category for each unique cluster
    for i, category in enumerate(predicted_categories.unique()):
        print(f"Cluster {i} diprediksi sebagai: {category}")
else:
    print("Kolom 'RestingBP' tidak ditemukan dalam dataset.")
