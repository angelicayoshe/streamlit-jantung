# -*- coding: utf-8 -*-
"""
Created on Sat May 18 10:41:14 2024

@author: User
"""

import numpy as np
import pickle
import streamlit as st

def predict_disease_category(input_data):
    # Mendapatkan nilai restingBP dari input_data
    restingBP_range = input_data[2]  # Indeks 2 mengacu pada kolom RestingBP
    
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



def main():
    # Memberi judul
    st.title('Heart Diseases Web App')
    
    # Mendapatkan input data dari pengguna
    Age = st.text_input('Age of the Person')
    Sex = st.text_input('Sex (0 for Male and 1 for Female)')
    RestingBP = st.text_input('RestingBP value')
    Cholesterol = st.text_input('Cholesterol value')
    MaxHR = st.text_input('MaxHR value')
    Oldpeak = st.text_input('Oldpeak value')
    
    # Code untuk prediksi
    diagnosis = ''
    
    # Membuat tombol untuk prediksi
    if st.button('Heart Diseases Test Result'):
        try:
            # Mengonversi input menjadi tipe data numerik
            Age = float(Age)
            Sex = int(Sex)
            RestingBP = float(RestingBP)
            Cholesterol = float(Cholesterol)
            MaxHR = float(MaxHR)
            Oldpeak = float(Oldpeak)
            
            # Memastikan bentuk input sesuai dengan yang diharapkan
            input_data = np.array([Age, Sex, RestingBP, Cholesterol, MaxHR, Oldpeak])
            
            # Memanggil fungsi prediksi dengan input yang dikonversi
            diagnosis = predict_disease_category(input_data)
            st.success(f'Diagnosis: {diagnosis}')
        except ValueError as e:
            st.error(f'Please enter valid numeric values for all inputs. Error: {e}')
        except Exception as e:
            st.error(f'An unexpected error occurred. Error: {e}')
    
if __name__ == '__main__':
    main()
